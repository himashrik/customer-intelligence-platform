import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Reproducible data
np.random.seed(42)
random.seed(42)

# -----------------------------
# Configuration
# -----------------------------

NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 100
NUM_ORDERS = 5000

# -----------------------------
# Customers
# -----------------------------

first_names = [
    "Aarav", "Aditya", "Arjun", "Ananya", "Diya",
    "Ishaan", "Kavya", "Meera", "Neha", "Rahul",
    "Riya", "Rohan", "Sneha", "Varun", "Vikram"
]

last_names = [
    "Sharma", "Reddy", "Kumar", "Patel", "Singh",
    "Gupta", "Rao", "Verma", "Joshi", "Nair"
]

countries = [
    "India",
    "USA",
    "UK",
    "Canada",
    "Australia",
    "Germany"
]

customers = []

start_date = datetime(2023, 1, 1)

for i in range(1, NUM_CUSTOMERS + 1):

    name = f"{random.choice(first_names)} {random.choice(last_names)}"

    signup_date = start_date + timedelta(
        days=random.randint(0, 700)
    )

    customers.append({
        "customer_id": i,
        "name": name,
        "email": f"customer{i}@example.com",
        "country": random.choice(countries),
        "signup_date": signup_date.date()
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# Products
# -----------------------------

categories = {
    "Electronics": [
        "Wireless Headphones",
        "Smart Watch",
        "Bluetooth Speaker",
        "Power Bank",
        "USB Cable"
    ],
    "Clothing": [
        "T-Shirt",
        "Jeans",
        "Hoodie",
        "Jacket",
        "Sneakers"
    ],
    "Home": [
        "Coffee Maker",
        "Table Lamp",
        "Bedsheet",
        "Kitchen Set",
        "Wall Clock"
    ],
    "Beauty": [
        "Face Wash",
        "Moisturizer",
        "Shampoo",
        "Perfume",
        "Lip Balm"
    ],
    "Books": [
        "Python Programming",
        "Data Science",
        "Machine Learning",
        "Database Systems",
        "Web Development"
    ]
}

products = []

product_id = 1

for category, product_names in categories.items():

    for name in product_names:

        # Generate multiple variants
        for _ in range(NUM_PRODUCTS // len(categories) // len(product_names)):

            products.append({
                "product_id": product_id,
                "product_name": name,
                "category": category,
                "price": round(
                    random.uniform(10, 500),
                    2
                )
            })

            product_id += 1

# Make sure we have 100 products
while len(products) < NUM_PRODUCTS:

    category = random.choice(list(categories.keys()))

    products.append({
        "product_id": len(products) + 1,
        "product_name": random.choice(categories[category]),
        "category": category,
        "price": round(random.uniform(10, 500), 2)
    })

products_df = pd.DataFrame(products[:NUM_PRODUCTS])

# -----------------------------
# Orders
# -----------------------------

orders = []

order_start = datetime(2023, 1, 1)
order_end = datetime(2025, 12, 31)

for order_id in range(1, NUM_ORDERS + 1):

    customer_id = random.randint(
        1,
        NUM_CUSTOMERS
    )

    random_days = random.randint(
        0,
        (order_end - order_start).days
    )

    order_date = order_start + timedelta(
        days=random_days
    )

    # Generate 1-5 products per order
    num_items = random.randint(1, 5)

    selected_products = random.sample(
        products,
        num_items
    )

    total_amount = 0

    for product in selected_products:

        quantity = random.randint(1, 3)

        total_amount += (
            product["price"] * quantity
        )

    orders.append({
        "order_id": order_id,
        "customer_id": customer_id,
        "order_date": order_date,
        "total_amount": round(total_amount, 2)
    })

orders_df = pd.DataFrame(orders)

# -----------------------------
# Order Items
# -----------------------------

order_items = []

for order in orders:

    num_items = random.randint(1, 5)

    selected_products = random.sample(
        products,
        num_items
    )

    for product in selected_products:

        quantity = random.randint(1, 3)

        order_items.append({
            "order_id": order["order_id"],
            "product_id": product["product_id"],
            "quantity": quantity,
            "unit_price": product["price"]
        })

order_items_df = pd.DataFrame(order_items)

# -----------------------------
# Save CSV files
# -----------------------------

customers_df.to_csv(
    "customers.csv",
    index=False
)

products_df.to_csv(
    "products.csv",
    index=False
)

orders_df.to_csv(
    "orders.csv",
    index=False
)

order_items_df.to_csv(
    "order_items.csv",
    index=False
)

print("Data generation completed!")

print(f"Customers: {len(customers_df)}")
print(f"Products: {len(products_df)}")
print(f"Orders: {len(orders_df)}")
print(f"Order Items: {len(order_items_df)}")