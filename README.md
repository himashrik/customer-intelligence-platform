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
```markdown

✨ Key Features
📊 Business Analytics
Total customers
Total orders
Total revenue
Average order value
Monthly revenue trends
Top customers
Top products
Category performance
Country performance
👥 RFM Customer Segmentation

Customers are segmented using:

Recency — how recently a customer purchased
Frequency — how frequently a customer purchases
Monetary — how much a customer spends

Customer segments include:

Champions
Loyal Customers
Potential Loyalists
New Customers
At Risk
Lost Customers
🤖 Customer Churn Prediction

A machine learning model predicts customers who are likely to churn.

Features include:

Recency
Frequency
Monetary value
Average order value

The model uses:

Logistic Regression + StandardScaler

Customers are classified into:

High Risk
Medium Risk
Low Risk
📈 Power BI Dashboard

The Power BI dashboard provides interactive visualizations for:

Revenue trends
Customer segmentation
Product/category performance
Churn risk
High-risk customers
Country performance
🛠️ Tech Stack
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
MySQL / MariaDB
Machine Learning
Python
Pandas
NumPy
Scikit-learn
Logistic Regression
Joblib
Business Intelligence
Microsoft Power BI
Development Tools
Git
GitHub
VS Code
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
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── ml/
│   ├── churn_prediction.py
│   ├── churn_predictions.csv
│   └── load_churn.py
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
🔌 API Endpoints
Endpoint	Description
/	API status
/health	Health check
/customers	Customer data
/analytics/kpis	Business KPIs
/analytics/revenue	Monthly revenue
/analytics/customers	Top customers
/analytics/segments	RFM segments
/analytics/products	Top products
/analytics/countries	Country performance
/analytics/categories	Category performance
/analytics/churn	Churn analysis
/analytics/churn/customers	High-risk customers
🚀 Running the Project
1. Clone the repository
git clone https://github.com/himashrik/customer-intelligence-platform.git

cd customer-intelligence-platform
2. Backend setup
cd backend

python -m venv venv

Activate the environment on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure the database connection using an environment variable:

DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/customer_intelligence

Start the API:

uvicorn main:app --reload

API:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
3. Frontend setup

Open another terminal:

cd frontend

npm install

npm run dev

Frontend:

http://localhost:5173
4. Machine Learning

From the ml directory:

python churn_prediction.py

This generates the churn prediction results.

📊 Dataset

The project uses a customer transaction dataset containing:

1,000 customers
100 products
5,000 orders
Order item-level transaction data

The transaction data covers multiple countries and product categories.

📈 Business Results

The analytics pipeline produces insights such as:

Revenue and order trends
High-value customers
Customer segments
Product performance
Geographic performance
Customers at risk of churn
Revenue potentially affected by customer churn
🎯 Business Use Cases

This platform can help businesses:

Identify high-value customers
Improve customer retention
Detect potential churn
Target customer segments
Optimize marketing campaigns
Analyze product performance
Monitor revenue trends
Support data-driven decision making
👩‍💻 Author

Himashri Kandi

B.Tech — Information Technology

GitHub: https://github.com/himashrik

⭐ If you find this project useful, consider giving it a star!