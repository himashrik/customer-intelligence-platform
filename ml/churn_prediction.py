import os
import joblib
import pandas as pd

from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/customer_intelligence"

engine = create_engine(DATABASE_URL)


# --------------------------------------------------
# CREATE TRAINING DATA
# --------------------------------------------------

query = """
SELECT
    c.customer_id,

    COUNT(o.order_id) AS frequency,

    COALESCE(SUM(o.total_amount), 0) AS monetary,

    DATEDIFF(
        '2025-06-30',
        MAX(o.order_date)
    ) AS recency,

    AVG(o.total_amount) AS average_order_value

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id
    AND o.order_date <= '2025-06-30'

GROUP BY c.customer_id
"""


df = pd.read_sql(query, engine)


# --------------------------------------------------
# CLEAN DATA
# --------------------------------------------------

df["frequency"] = df["frequency"].fillna(0)
df["monetary"] = df["monetary"].fillna(0)
df["average_order_value"] = df["average_order_value"].fillna(0)

df["recency"] = df["recency"].fillna(9999)


# --------------------------------------------------
# CREATE CHURN LABEL
# --------------------------------------------------
# Customer is considered churned if they did not
# purchase during the following 90 days.
#
# Observation date: 2025-06-30
# Churn window:     2025-07-01 → 2025-09-28
# --------------------------------------------------

future_orders_query = """
SELECT DISTINCT customer_id
FROM orders
WHERE order_date > '2025-06-30'
AND order_date <= '2025-09-28'
"""

future_orders = pd.read_sql(
    future_orders_query,
    engine
)

future_customer_ids = set(
    future_orders["customer_id"]
)


df["churn"] = df["customer_id"].apply(
    lambda customer_id:
        0 if customer_id in future_customer_ids else 1
)


# --------------------------------------------------
# DISPLAY DATASET
# --------------------------------------------------

print("\nTraining Dataset:")
print(df.head())

print("\nChurn Distribution:")
print(df["churn"].value_counts())


# --------------------------------------------------
# FEATURES
# --------------------------------------------------

features = [
    "recency",
    "frequency",
    "monetary",
    "average_order_value"
]

X = df[features]
y = df["churn"]


# --------------------------------------------------
# TRAIN / TEST SPLIT
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# MACHINE LEARNING PIPELINE
# --------------------------------------------------

model = Pipeline([
    (
        "scaler",
        StandardScaler()
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000
        )
    )
])


# --------------------------------------------------
# TRAIN MODEL
# --------------------------------------------------

model.fit(
    X_train,
    y_train
)


# --------------------------------------------------
# EVALUATE
# --------------------------------------------------

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]


print("\nModel Performance")
print("-----------------------------")

print(
    "Accuracy:",
    round(
        accuracy_score(y_test, predictions),
        4
    )
)

print(
    "ROC-AUC:",
    round(
        roc_auc_score(y_test, probabilities),
        4
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)


# --------------------------------------------------
# PREDICT ALL CUSTOMERS
# --------------------------------------------------

df["churn_probability"] = (
    model.predict_proba(
        df[features]
    )[:, 1]
)


df["churn_prediction"] = (
    df["churn_probability"]
    >= 0.5
).astype(int)


# --------------------------------------------------
# CHURN RISK CATEGORY
# --------------------------------------------------

def risk_category(probability):

    if probability >= 0.70:
        return "High Risk"

    elif probability >= 0.40:
        return "Medium Risk"

    else:
        return "Low Risk"


df["risk_category"] = (
    df["churn_probability"]
    .apply(risk_category)
)


# --------------------------------------------------
# SAVE PREDICTIONS
# --------------------------------------------------

output_file = os.path.join(
    os.path.dirname(__file__),
    "churn_predictions.csv"
)

df.to_csv(
    output_file,
    index=False
)


# --------------------------------------------------
# SAVE MODEL
# --------------------------------------------------

model_file = os.path.join(
    os.path.dirname(__file__),
    "churn_model.pkl"
)

joblib.dump(
    model,
    model_file
)


print("\nFiles created:")
print(output_file)
print(model_file)


print("\nTop Churn Risk Customers:")

print(
    df[
        [
            "customer_id",
            "recency",
            "frequency",
            "monetary",
            "churn_probability",
            "risk_category"
        ]
    ]
    .sort_values(
        "churn_probability",
        ascending=False
    )
    .head(10)
)
