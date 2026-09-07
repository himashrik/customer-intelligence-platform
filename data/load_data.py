import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# ---------------------------------------
# Database configuration
# ---------------------------------------

DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/customer_intelligence"

engine = create_engine(DATABASE_URL)

# ---------------------------------------
# Data folder
# ---------------------------------------

DATA_DIR = Path(__file__).parent

# ---------------------------------------
# Load CSV files
# ---------------------------------------

print("\nLoading CSV files...")

customers = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
orders = pd.read_csv(DATA_DIR / "orders.csv")
order_items = pd.read_csv(DATA_DIR / "order_items.csv")

print(f"Customers   : {len(customers)}")
print(f"Products    : {len(products)}")
print(f"Orders      : {len(orders)}")
print(f"Order Items : {len(order_items)}")

# ---------------------------------------
# Convert dates
# ---------------------------------------

customers["signup_date"] = pd.to_datetime(
    customers["signup_date"]
)

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

# ---------------------------------------
# Load data into MySQL
# ---------------------------------------

print("\nUploading customers...")

customers.to_sql(
    "customers",
    con=engine,
    if_exists="append",
    index=False
)

print("✅ Customers loaded")

print("\nUploading products...")

products.to_sql(
    "products",
    con=engine,
    if_exists="append",
    index=False
)

print("✅ Products loaded")

print("\nUploading orders...")

orders.to_sql(
    "orders",
    con=engine,
    if_exists="append",
    index=False
)

print("✅ Orders loaded")

print("\nUploading order items...")

order_items.to_sql(
    "order_items",
    con=engine,
    if_exists="append",
    index=False
)

print("✅ Order items loaded")

print("\n" + "=" * 50)
print("🎉 DATA LOAD COMPLETED SUCCESSFULLY")
print("=" * 50)