🚀 Customer Intelligence & Business Analytics Platform

An end-to-end customer analytics platform that combines React, FastAPI, MySQL/MariaDB, RFM segmentation, Machine Learning, and Power BI to understand customer behavior, identify high-risk customers, and support retention decisions.

🌐 Project Overview

Layer

Technology

Frontend

React.js, Vite, Axios, Recharts

Backend

Python, FastAPI, SQLAlchemy

Database

MySQL / MariaDB

Analytics

SQL, Pandas, NumPy

Machine Learning

Scikit-learn, Logistic Regression

Segmentation

RFM Analysis

BI

Power BI

Version Control

Git, GitHub

✨ Key Features

📊 Interactive business analytics dashboard

👥 RFM-based customer segmentation

🤖 ML-powered churn prediction

⚠️ High / Medium / Low churn-risk classification

📈 Revenue and order trend analysis

🛍️ Product and category performance

🌍 Country-wise business analysis

📥 CSV export for analytical data

🔌 REST APIs with FastAPI

🌙 Responsive React dashboard with dark mode

📊 Power BI business intelligence dashboard

🏗️ Architecture

React Frontend
      │
      │ REST API
      ▼
FastAPI Backend
      │
      │ SQLAlchemy
      ▼
MySQL / MariaDB
      │
      ├───────────────┐
      ▼               ▼
 RFM Analysis    Churn Prediction
      │               │
      └───────┬───────┘
              ▼
          Power BI

📸 Screenshots
<img width="1886" height="852" alt="Screenshot 2026-09-07 175528" src="https://github.com/user-attachments/assets/e08759cd-d251-4b7c-bc54-9c7ab76cb106" />
<img width="1897" height="862" alt="Screenshot 2026-09-07 175511" src="https://github.com/user-attachments/assets/bc99f1d0-18cb-4054-b376-de35e55435d8" />
<img width="1900" height="865" alt="Screenshot 2026-09-07 175505" src="https://github.com/user-attachments/assets/0bf03dc6-677b-4d1f-a1c4-977f4365ebfc" />
<img width="1897" height="871" alt="Screenshot 2026-09-07 175454" src="https://github.com/user-attachments/assets/3054be87-65f3-4fb6-883d-82f8fe594fa3" />
<img width="1901" height="871" alt="Screenshot 2026-09-07 175445" src="https://github.com/user-attachments/assets/28967949-5313-4782-afab-f905db66ddb6" />
<img width="1900" height="866" alt="Screenshot 2026-09-07 175427" src="https://github.com/user-attachments/assets/7b440465-a35d-4819-9578-fbe9a9b73775" />
<img width="1901" height="867" alt="Screenshot 2026-09-07 175408" src="https://github.com/user-attachments/assets/9c8b2330-21af-4688-a8d6-8ee5ffa0789d" />




Dashboard

Customer Segments

Churn Prediction

Add screenshot

Add screenshot

Add screenshot

🎯 RFM Customer Segmentation

RFM evaluates customers using three behavioral metrics:

Metric

Measures

Recency

How recently a customer purchased

Frequency

How often a customer purchases

Monetary

How much a customer spends

Segments

Champions · Loyal Customers · Potential Loyalists · New Customers · At Risk · Lost Customers

The analysis helps identify valuable customers and prioritize retention campaigns.

🤖 Churn Prediction

The ML pipeline uses historical customer purchasing behavior to estimate churn probability.

Features: Recency, Frequency, Monetary Value, Average Order Value

Transaction Data
      ↓
Feature Engineering
      ↓
RFM + AOV Features
      ↓
Train / Test Split
      ↓
StandardScaler
      ↓
Logistic Regression
      ↓
Churn Probability
      ↓
Risk Classification

Probability

Risk

≥ 70%

🔴 High Risk

≥ 40%

🟠 Medium Risk

< 40%

🟢 Low Risk

📊 Project Results

Metric

Result

Customers

1,000

Customers with Orders

994

Products

100

Orders

5,000

Total Revenue

7,361,180.78

Average Order Value

1,472.24

RFM Results

Segment

Customers

At Risk

286

New Customers

232

Potential Loyalists

166

Loyal Customers

128

Lost Customers

112

Champions

70

Churn Results

Risk Category

Customers

🔴 High Risk

380

🟠 Medium Risk

620

🟢 Low Risk

0

Key business insight: The At Risk segment is the largest RFM group, making customer retention an important business opportunity.

🔌 REST API

FastAPI provides endpoints for:

GET /health
GET /customers
GET /analytics/kpis
GET /analytics/revenue
GET /analytics/customers
GET /analytics/segments
GET /analytics/products
GET /analytics/countries
GET /analytics/categories
GET /analytics/churn
GET /analytics/churn/customers

Local API documentation:

http://127.0.0.1:8000/docs

🗄️ Database

customer_intelligence
│
├── customers
├── products
├── orders
├── order_items
├── customer_segments
└── churn_predictions

Main relationships connect customers to orders, orders to order items, products to order items, and customers to their RFM and churn results.

📁 Project Structure

customer-intelligence-platform/
├── backend/
├── data/
├── frontend/
├── ml/
├── notebooks/
├── powerbi/
├── sql/
├── .gitignore
└── README.md

⚙️ Run Locally

1. Clone

git clone https://github.com/himashrik/customer-intelligence-platform.git
cd customer-intelligence-platform

2. Database

Create the database:

CREATE DATABASE customer_intelligence;

Configure backend/.env:

DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/customer_intelligence

3. Backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

4. Frontend

Open another terminal:

cd frontend
npm install
npm run dev

📌 Business Use Cases

Identify high-value customers

Detect customers at risk of churn

Prioritize retention campaigns

Monitor revenue trends

Compare product and category performance

Analyze geographic customer performance

Support data-driven marketing decisions

🔮 Future Enhancements

Cloud deployment

Real-time analytics

Advanced ML models

Customer lifetime value prediction

Automated retention recommendations

Role-based authentication

Scheduled dashboard refresh

👨‍💻 Author

Himashri Kandi

B.Tech — Information Technology

GitHub: https://github.com/himashrik

⭐ If you find this project useful, consider giving the repository a star.
