import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://root:@127.0.0.1:3306/"
    "customer_intelligence"
)

engine = create_engine(DATABASE_URL)

df = pd.read_csv("churn_predictions.csv")

columns = [
    "customer_id",
    "recency",
    "frequency",
    "monetary",
    "average_order_value",
    "churn_probability",
    "churn_prediction",
    "risk_category"
]

df = df[columns]

df.to_sql(
    "churn_predictions",
    con=engine,
    if_exists="append",
    index=False
)

print("Churn predictions loaded successfully!")
print(f"Rows loaded: {len(df)}")