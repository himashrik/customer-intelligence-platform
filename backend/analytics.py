from sqlalchemy import text
from sqlalchemy.orm import Session


def get_kpis(db: Session):
    query = text("""
        SELECT
            COUNT(DISTINCT customer_id) AS total_customers,
            COUNT(*) AS total_orders,
            ROUND(SUM(total_amount), 2) AS total_revenue,
            ROUND(AVG(total_amount), 2) AS average_order_value
        FROM orders;
    """)

    result = db.execute(query).mappings().first()

    return {
        "total_customers": result["total_customers"],
        "total_orders": result["total_orders"],
        "total_revenue": float(result["total_revenue"]),
        "average_order_value": float(result["average_order_value"])
    }


def get_revenue_by_month(db: Session):
    query = text("""
        SELECT
            DATE_FORMAT(order_date, '%Y-%m') AS month,
            ROUND(SUM(total_amount), 2) AS revenue
        FROM orders
        GROUP BY DATE_FORMAT(order_date, '%Y-%m')
        ORDER BY month;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "month": row["month"],
            "revenue": float(row["revenue"])
        }
        for row in result
    ]


def get_top_customers(db: Session):
    query = text("""
        SELECT
            c.customer_id,
            c.name,
            c.country,
            COUNT(o.order_id) AS orders,
            ROUND(SUM(o.total_amount), 2) AS total_spent
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        GROUP BY
            c.customer_id,
            c.name,
            c.country
        ORDER BY total_spent DESC
        LIMIT 10;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "customer_id": row["customer_id"],
            "name": row["name"],
            "country": row["country"],
            "orders": row["orders"],
            "total_spent": float(row["total_spent"])
        }
        for row in result
    ]


def get_segments(db: Session):
    query = text("""
        SELECT
            segment,
            COUNT(*) AS customers,
            ROUND(AVG(monetary), 2) AS avg_customer_value,
            ROUND(SUM(monetary), 2) AS total_revenue
        FROM customer_segments
        GROUP BY segment
        ORDER BY total_revenue DESC;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "segment": row["segment"],
            "customers": row["customers"],
            "avg_customer_value": float(row["avg_customer_value"]),
            "total_revenue": float(row["total_revenue"])
        }
        for row in result
    ]


def get_top_products(db: Session):
    query = text("""
        SELECT
            p.product_id,
            p.product_name,
            p.category,
            SUM(oi.quantity) AS units_sold,
            ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
        FROM products p
        JOIN order_items oi
            ON p.product_id = oi.product_id
        GROUP BY
            p.product_id,
            p.product_name,
            p.category
        ORDER BY revenue DESC
        LIMIT 10;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "product_id": row["product_id"],
            "product_name": row["product_name"],
            "category": row["category"],
            "units_sold": row["units_sold"],
            "revenue": float(row["revenue"])
        }
        for row in result
    ]


def get_country_performance(db: Session):
    query = text("""
        SELECT
            c.country,
            COUNT(DISTINCT c.customer_id) AS customers,
            COUNT(o.order_id) AS orders,
            ROUND(SUM(o.total_amount), 2) AS revenue
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        GROUP BY c.country
        ORDER BY revenue DESC;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "country": row["country"],
            "customers": row["customers"],
            "orders": row["orders"],
            "revenue": float(row["revenue"])
        }
        for row in result
    ]
def get_churn_analysis(db: Session):
    query = text("""
        SELECT
            risk_category,
            COUNT(*) AS customers,
            ROUND(
                AVG(churn_probability) * 100,
                2
            ) AS avg_churn_probability,
            ROUND(
                SUM(monetary),
                2
            ) AS revenue_at_risk
        FROM churn_predictions
        GROUP BY risk_category
        ORDER BY avg_churn_probability DESC;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "risk_category": row["risk_category"],
            "customers": row["customers"],
            "avg_churn_probability": float(
                row["avg_churn_probability"]
            ),
            "revenue_at_risk": float(
                row["revenue_at_risk"]
            )
        }
        for row in result
    ]
def get_high_risk_customers(db: Session):
    query = text("""
        SELECT
            cp.customer_id,
            c.name,
            c.country,
            cp.recency,
            cp.frequency,
            cp.monetary,
            cp.churn_probability,
            cp.risk_category
        FROM churn_predictions cp
        JOIN customers c
            ON cp.customer_id = c.customer_id
        ORDER BY cp.churn_probability DESC
        LIMIT 10;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "customer_id": row["customer_id"],
            "name": row["name"],
            "country": row["country"],
            "recency": row["recency"],
            "frequency": row["frequency"],
            "monetary": float(row["monetary"]),
            "churn_probability": float(row["churn_probability"]),
            "risk_category": row["risk_category"]
        }
        for row in result
    ]
from sqlalchemy import text
from sqlalchemy.orm import Session


def get_category_performance(db: Session):
    query = text("""
        SELECT
            p.category,
            SUM(oi.quantity) AS units_sold,
            ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
        FROM products p
        JOIN order_items oi
            ON p.product_id = oi.product_id
        GROUP BY p.category
        ORDER BY revenue DESC;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "category": row["category"],
            "units_sold": int(row["units_sold"]),
            "revenue": float(row["revenue"])
        }
        for row in result
    ]


def get_customer_summary(db: Session):
    query = text("""
        SELECT
            c.customer_id,
            c.name,
            c.email,
            c.country,
            c.signup_date,
            COUNT(o.order_id) AS orders,
            ROUND(COALESCE(SUM(o.total_amount), 0), 2) AS total_spent,
            ROUND(
                COALESCE(AVG(o.total_amount), 0), 2
            ) AS average_order_value,
            MAX(o.order_date) AS last_order
        FROM customers c
        LEFT JOIN orders o
            ON c.customer_id = o.customer_id
        GROUP BY
            c.customer_id,
            c.name,
            c.email,
            c.country,
            c.signup_date
        ORDER BY total_spent DESC;
    """)

    result = db.execute(query).mappings().all()

    return [
        {
            "customer_id": row["customer_id"],
            "name": row["name"],
            "email": row["email"],
            "country": row["country"],
            "signup_date": str(row["signup_date"])
            if row["signup_date"]
            else None,
            "orders": int(row["orders"]),
            "total_spent": float(row["total_spent"]),
            "average_order_value": float(
                row["average_order_value"]
            ),
            "last_order": str(row["last_order"])
            if row["last_order"]
            else None
        }
        for row in result
    ]