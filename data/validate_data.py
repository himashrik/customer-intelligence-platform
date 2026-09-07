import pandas as pd
import os

print("=" * 60)
print("CUSTOMER INTELLIGENCE PLATFORM - DATA VALIDATION")
print("=" * 60)


def load_file(filename):
    path = os.path.join(os.path.dirname(__file__), filename)

    if not os.path.exists(path):
        print(f"❌ File not found: {filename}")
        return None

    return pd.read_csv(path)


# Load datasets
customers = load_file("customers.csv")
products = load_file("products.csv")
orders = load_file("orders.csv")
order_items = load_file("order_items.csv")


datasets = {
    "Customers": customers,
    "Products": products,
    "Orders": orders,
    "Order Items": order_items
}


# --------------------------------------------------
# Basic Information
# --------------------------------------------------

print("\n📊 DATASET SIZES")
print("-" * 60)

for name, df in datasets.items():

    if df is not None:
        print(f"{name:<15}: {len(df):>6} rows")


# --------------------------------------------------
# Missing Values
# --------------------------------------------------

print("\n🔍 MISSING VALUES")
print("-" * 60)

for name, df in datasets.items():

    if df is not None:

        missing = df.isnull().sum()

        total_missing = missing.sum()

        if total_missing == 0:
            print(f"✅ {name}: No missing values")

        else:
            print(f"⚠️ {name}:")
            print(missing[missing > 0])


# --------------------------------------------------
# Duplicate Records
# --------------------------------------------------

print("\n🔁 DUPLICATE RECORDS")
print("-" * 60)

for name, df in datasets.items():

    if df is not None:

        duplicates = df.duplicated().sum()

        if duplicates == 0:
            print(f"✅ {name}: No duplicates")

        else:
            print(f"⚠️ {name}: {duplicates} duplicates")


# --------------------------------------------------
# Negative Values
# --------------------------------------------------

print("\n💰 NEGATIVE VALUE CHECK")
print("-" * 60)

if products is not None:

    negative_prices = (products["price"] < 0).sum()

    if negative_prices == 0:
        print("✅ Products: No negative prices")
    else:
        print(f"⚠️ Products: {negative_prices} negative prices")


if orders is not None:

    negative_orders = (orders["total_amount"] < 0).sum()

    if negative_orders == 0:
        print("✅ Orders: No negative order amounts")
    else:
        print(f"⚠️ Orders: {negative_orders} negative amounts")


# --------------------------------------------------
# Referential Integrity
# --------------------------------------------------

print("\n🔗 REFERENTIAL INTEGRITY")
print("-" * 60)

if customers is not None and orders is not None:

    invalid_customers = (
        ~orders["customer_id"].isin(
            customers["customer_id"]
        )
    ).sum()

    if invalid_customers == 0:
        print("✅ Orders → Customers: Valid")
    else:
        print(
            f"⚠️ Orders → Customers: "
            f"{invalid_customers} invalid references"
        )


if orders is not None and order_items is not None:

    invalid_orders = (
        ~order_items["order_id"].isin(
            orders["order_id"]
        )
    ).sum()

    if invalid_orders == 0:
        print("✅ Order Items → Orders: Valid")
    else:
        print(
            f"⚠️ Order Items → Orders: "
            f"{invalid_orders} invalid references"
        )


if products is not None and order_items is not None:

    invalid_products = (
        ~order_items["product_id"].isin(
            products["product_id"]
        )
    ).sum()

    if invalid_products == 0:
        print("✅ Order Items → Products: Valid")
    else:
        print(
            f"⚠️ Order Items → Products: "
            f"{invalid_products} invalid references"
        )


# --------------------------------------------------
# Date Validation
# --------------------------------------------------

print("\n📅 DATE VALIDATION")
print("-" * 60)

if customers is not None:

    customers["signup_date"] = pd.to_datetime(
        customers["signup_date"],
        errors="coerce"
    )

    invalid_dates = customers["signup_date"].isnull().sum()

    if invalid_dates == 0:
        print("✅ Customer signup dates: Valid")
    else:
        print(
            f"⚠️ Customer signup dates: "
            f"{invalid_dates} invalid"
        )


if orders is not None:

    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )

    invalid_dates = orders["order_date"].isnull().sum()

    if invalid_dates == 0:
        print("✅ Order dates: Valid")
    else:
        print(
            f"⚠️ Order dates: "
            f"{invalid_dates} invalid"
        )


# --------------------------------------------------
# Summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("VALIDATION COMPLETED")
print("=" * 60)