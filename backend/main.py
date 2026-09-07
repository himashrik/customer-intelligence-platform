from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import get_db
from models import Customer

from analytics import (
    get_kpis,
    get_revenue_by_month,
    get_top_customers,
    get_segments,
    get_top_products,
    get_country_performance,
    get_churn_analysis,
    get_high_risk_customers,
    get_category_performance,
    get_customer_summary
)


# Create FastAPI application
app = FastAPI(
    title="Customer Intelligence Platform",
    description="Analytics and customer intelligence backend",
    version="1.0.0"
)


# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home
@app.get("/")
def home():
    return {
        "message": "Customer Intelligence Platform API is running!"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# Get customers
@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()
    return customers


# Analytics - KPIs
@app.get("/analytics/kpis")
def analytics_kpis(db: Session = Depends(get_db)):
    return get_kpis(db)


# Analytics - Monthly Revenue
@app.get("/analytics/revenue")
def analytics_revenue(db: Session = Depends(get_db)):
    return get_revenue_by_month(db)


# Analytics - Top Customers
@app.get("/analytics/customers")
def analytics_customers(db: Session = Depends(get_db)):
    return get_top_customers(db)


# Analytics - Customer Segments
@app.get("/analytics/segments")
def analytics_segments(db: Session = Depends(get_db)):
    return get_segments(db)


# Analytics - Top Products
@app.get("/analytics/products")
def analytics_products(db: Session = Depends(get_db)):
    return get_top_products(db)


# Analytics - Country Performance
@app.get("/analytics/countries")
def analytics_countries(db: Session = Depends(get_db)):
    return get_country_performance(db)
@app.get("/analytics/churn")
def analytics_churn(db: Session = Depends(get_db)):
    return get_churn_analysis(db)
@app.get("/analytics/churn/customers")
def churn_customers(db: Session = Depends(get_db)):
    return get_high_risk_customers(db)
@app.get("/analytics/categories")
def analytics_categories(db: Session = Depends(get_db)):
    return get_category_performance(db)


@app.get("/analytics/customer-summary")
def customer_summary(db: Session = Depends(get_db)):
    return get_customer_summary(db)