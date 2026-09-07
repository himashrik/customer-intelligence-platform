# 🚀 Customer Intelligence & Business Analytics Platform

An end-to-end **Customer Intelligence and Business Analytics Platform** that combines business analytics, RFM customer segmentation, machine learning-based churn prediction, REST APIs, an interactive React dashboard, and Power BI.

The platform helps businesses understand customer behavior, identify high-value and at-risk customers, analyze sales performance, and make data-driven customer retention decisions.

---

## 📌 Project Overview

Customer retention is an important challenge for businesses because losing existing customers can directly affect revenue.

This project provides a centralized analytics platform that transforms customer transaction data into actionable business insights.

The system performs:

- Customer analytics
- Sales and revenue analysis
- RFM customer segmentation
- Customer churn prediction
- Product and category analysis
- Country-wise performance analysis
- High-risk customer identification
- Interactive data visualization
- Power BI business intelligence reporting

---

# 🎯 Objectives

The main objectives of this project are:

1. Analyze customer purchasing behavior.
2. Identify high-value customers.
3. Segment customers using RFM analysis.
4. Predict customers who are likely to churn.
5. Identify high-risk customers.
6. Analyze revenue and sales trends.
7. Analyze product and category performance.
8. Analyze country-wise business performance.
9. Provide REST APIs for analytics.
10. Build interactive dashboards for business decision-making.

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────────┐
                         │      React Frontend     │
                         │                         │
                         │  Interactive Dashboard  │
                         └────────────┬────────────┘
                                      │
                                      │ REST API
                                      ▼
                         ┌─────────────────────────┐
                         │     FastAPI Backend     │
                         │                         │
                         │ Analytics REST APIs     │
                         └────────────┬────────────┘
                                      │
                                      │ SQLAlchemy
                                      ▼
                         ┌─────────────────────────┐
                         │     MySQL / MariaDB     │
                         │                         │
                         │  Customers              │
                         │  Products               │
                         │  Orders                 │
                         │  Order Items            │
                         │  Customer Segments      │
                         │  Churn Predictions      │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
                    ▼                                   ▼
          ┌─────────────────────┐             ┌─────────────────────┐
          │   RFM Analysis      │             │  Churn Prediction  │
          │                     │             │                     │
          │ Recency             │             │ Logistic Regression │
          │ Frequency           │             │                     │
          │ Monetary            │             │ Customer Risk       │
          └──────────┬──────────┘             └──────────┬──────────┘
                     │                                   │
                     └─────────────────┬─────────────────┘
                                       ▼
                           ┌─────────────────────────┐
                           │       Power BI          │
                           │                         │
                           │ Business Intelligence   │
                           │ Dashboard               │
                           └─────────────────────────┘
✨ Key Features
📊 1. Business Analytics

The platform provides important business KPIs including:

Total Customers
Total Orders
Total Revenue
Average Order Value
Monthly Revenue
Top Customers
Top Products
Category Performance
Country Performance
Customer Purchase Frequency
👥 2. RFM Customer Segmentation

The platform uses RFM Analysis to understand customer value and behavior.

Recency

Measures how recently a customer made a purchase.

A lower number of days indicates a more recent purchase.

Frequency

Measures how frequently a customer places orders.

Higher frequency indicates stronger customer engagement.

Monetary

Measures the total amount spent by a customer.

Higher monetary value indicates a more valuable customer.

🧩 Customer Segments

The RFM analysis classifies customers into:

Segment	Description
🏆 Champions	Highly valuable and highly engaged customers
💙 Loyal Customers	Customers who purchase frequently
🌱 Potential Loyalists	Customers with potential to become loyal
🆕 New Customers	Recently acquired customers
⚠️ At Risk	Customers showing signs of reduced engagement
🔴 Lost Customers	Customers with low recent engagement and purchasing activity
🤖 3. Machine Learning Churn Prediction

The project uses Machine Learning to predict customers who are likely to churn.

The model analyzes customer transaction behavior and predicts churn probability.

Features Used

The model uses:

Recency
Frequency
Monetary Value
Average Order Value
Machine Learning Pipeline
Customer Transaction Data
          │
          ▼
Feature Engineering
          │
          ▼
Recency
Frequency
Monetary
Average Order Value
          │
          ▼
Train / Test Split
          │
          ▼
StandardScaler
          │
          ▼
Logistic Regression
          │
          ▼
Churn Probability
          │
          ▼
Risk Classification
⚠️ Churn Risk Classification

Customers are classified according to predicted churn probability.

Probability	Risk Category
≥ 70%	High Risk
≥ 40%	Medium Risk
< 40%	Low Risk

The system can therefore help businesses prioritize customers who require retention strategies.

📈 4. Power BI Dashboard

The project includes an interactive Power BI dashboard.

The dashboard contains:

KPI Cards
Total Customers
Total Orders
Total Revenue
Average Order Value
Revenue Analysis
Monthly revenue trend
Revenue performance over time
Customer Analysis
RFM customer segments
Customer distribution
Top customers
Product Analysis
Product revenue
Category performance
Units sold
Churn Analysis
High-risk customers
Revenue at risk
Average churn probability
Churn risk distribution
Customer-level churn information
Geographic Analysis
Country-wise revenue
Country-wise customer performance
🖥️ React Dashboard

The React frontend provides an interactive business intelligence interface.

It includes:

Responsive dashboard
Sidebar navigation
KPI cards
Revenue charts
RFM segmentation chart
Category performance chart
Top customer table
Top product table
Churn analysis
High-risk customer table
Country performance
Business insights
CSV export functionality
Dark mode
🔌 REST API

The backend is developed using FastAPI.

API Endpoints
Endpoint	Description
/	API status
/health	Health check
/customers	Customer data
/analytics/kpis	Business KPIs
/analytics/revenue	Monthly revenue
/analytics/customers	Top customers
/analytics/segments	RFM customer segments
/analytics/products	Top products
/analytics/countries	Country performance
/analytics/categories	Category performance
/analytics/churn	Churn analysis
/analytics/churn/customers	High-risk customers
📚 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

http://127.0.0.1:8000/docs

This allows the API endpoints to be tested directly from the browser.

🗄️ Database Design

The project uses MySQL/MariaDB.

Database
customer_intelligence
Tables
customers

Stores customer information.

customer_id
name
email
country
signup_date
products

Stores product information.

product_id
product_name
category
price
orders

Stores customer order information.

order_id
customer_id
order_date
total_amount
order_items

Stores individual products within each order.

order_item_id
order_id
product_id
quantity
unit_price
customer_segments

Stores RFM segmentation results.

customer_id
name
recency
frequency
monetary
r_score
f_score
m_score
rfm_score
segment
churn_predictions

Stores machine learning churn predictions.

customer_id
recency
frequency
monetary
average_order_value
churn_probability
churn_prediction
risk_category
📊 Dataset

The project uses a transaction dataset containing:

1,000 customers
100 products
5,000 orders
Order-level transaction details
Multiple countries
Multiple product categories
Product Categories
Electronics
Clothing
Home
Beauty
Books
Countries
India
USA
UK
Canada
Germany
Australia
📈 Project Results

The analytics pipeline produced the following key results:

Metric	Value
Total Customers with Orders	994
Total Orders	5,000
Total Revenue	7,361,180.78
Average Order Value	1,472.24
👥 RFM Segmentation Results

The generated customer segmentation contains:

Segment	Customers
At Risk	286
New Customers	232
Potential Loyalists	166
Loyal Customers	128
Lost Customers	112
Champions	70

The At Risk segment represents a significant customer group that can be targeted through retention campaigns.

🤖 Churn Prediction Results

The churn model generated predictions for 1,000 customers.

Current risk distribution:

Risk Category	Customers
High Risk	380
Medium Risk	620
Low Risk	0
Revenue by Risk Category
Risk Category	Customer Monetary Value
High Risk	1,097,768.86
Medium Risk	5,029,820.42

These predictions can be used to prioritize customer retention efforts.

🌍 Country Performance

The platform analyzes customer and revenue performance across countries.

Country	Customers	Orders	Revenue
Germany	186	971	1,443,600.79
Australia	170	858	1,279,323.85
UK	170	883	1,273,399.06
Canada	164	801	1,210,285.08
India	161	792	1,165,400.43
USA	143	695	1,011,116.52
🛠️ Technology Stack
Frontend
React.js
Vite
Axios
Recharts
Lucide React
CSS
Backend
Python
FastAPI
SQLAlchemy
PyMySQL
REST APIs
Database
MySQL
MariaDB
Data Analysis
Pandas
NumPy
SQL
Machine Learning
Scikit-learn
Logistic Regression
StandardScaler
Joblib
Business Intelligence
Microsoft Power BI
Development Tools
Visual Studio Code
Git
GitHub
XAMPP
📂 Project Structure
customer-intelligence-platform/
│
├── backend/
│   ├── analytics.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── generate_data.py
│   ├── load_data.py
│   └── validate_data.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── ml/
│   ├── churn_prediction.py
│   ├── churn_predictions.csv
│   └── load_churn.py
│
├── notebooks/
│
├── powerbi/
│   └── Customer_Intelligence_Dashboard.pbix
│
├── sql/
│   ├── analytics.sql
│   ├── rfm_analysis.sql
│   └── rfm_segments.sql
│
├── .gitignore
└── README.md
🚀 Installation & Setup
1. Clone the Repository
git clone https://github.com/himashrik/customer-intelligence-platform.git
cd customer-intelligence-platform
🗄️ 2. Database Setup

Start MySQL/MariaDB.

Create the database:

CREATE DATABASE customer_intelligence;

Use the database:

USE customer_intelligence;

Create the required tables using the SQL scripts in:

sql/

The main tables are:

customers
products
orders
order_items
🐍 3. Backend Setup

Navigate to the backend:

cd backend

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
🔐 Database Configuration

Create a .env file inside the backend directory:

DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/customer_intelligence

Never commit .env files containing passwords, API keys, or other secrets.

▶️ 4. Start FastAPI Backend

From the backend directory:

uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs
📦 5. Load Dataset

Navigate to the data directory:

cd ../data

Generate the dataset:

python generate_data.py

Validate the dataset:

python validate_data.py

Load the data into MySQL/MariaDB:

python load_data.py
🤖 6. Run Churn Prediction

Navigate to the ML directory:

cd ../ml

Run:

python churn_prediction.py

The model generates:

churn_predictions.csv
churn_model.pkl

The generated predictions can then be loaded into the database using:

python load_churn.py
⚛️ 7. Frontend Setup

Open another terminal.

Navigate to:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

The frontend will be available at:

http://localhost:5173
📊 8. Power BI

The Power BI dashboard is available in:

powerbi/Customer_Intelligence_Dashboard.pbix

The dashboard connects to the MySQL/MariaDB database and provides interactive business intelligence visualizations.

🔄 Complete Data Flow
CSV Dataset
     │
     ▼
Data Validation
     │
     ▼
MySQL / MariaDB
     │
     ├───────────────┐
     │               │
     ▼               ▼
RFM Analysis      ML Churn Model
     │               │
     ▼               ▼
Customer         Churn
Segments         Predictions
     │               │
     └───────┬───────┘
             ▼
       FastAPI Backend
             │
             ▼
       React Dashboard
             │
             ▼
         Power BI
💡 Business Use Cases

The platform can be used for:

Customer Retention

Identify customers with high churn probability and target them with retention campaigns.

Customer Segmentation

Create personalized marketing campaigns based on RFM segments.

Revenue Analysis

Monitor revenue trends and identify high-performing periods.

Product Optimization

Identify products and categories generating the most revenue.

Geographic Analysis

Compare customer and revenue performance across different countries.

Customer Lifetime Value

Identify customers generating significant monetary value.

Business Decision Making

Provide data-driven insights for marketing, sales, and customer success teams.

🎯 Future Enhancements

Potential future improvements include:

Real-time customer analytics
Advanced churn models
Random Forest / XGBoost comparison
Customer Lifetime Value prediction
Automated retention recommendations
Email campaign integration
Role-based authentication
Cloud deployment
Automated model retraining
Advanced Power BI dashboards
Real-time data pipelines
🔒 Security

The project follows basic security practices such as:

Environment variables for database configuration
.gitignore for sensitive files
Separation of frontend and backend
API-based communication
Database access through SQLAlchemy

Sensitive credentials should never be committed to GitHub.

📌 Project Highlights

This project demonstrates practical knowledge of:

Full-stack development
REST API development
Database design
SQL analytics
Data preprocessing
Exploratory data analysis
Customer segmentation
Machine learning
Classification models
Business intelligence
Data visualization
Git and GitHub
👩‍💻 Author
Himashri Kandi

B.Tech – Information Technology

GitHub:

https://github.com/himashrik

⭐ Acknowledgement

This project was developed as a practical implementation of:

Data Analytics + Machine Learning + Full-Stack Development + Business Intelligence

⭐ If you found this project useful, consider giving it a star!