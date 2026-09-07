# 🚀 Customer Intelligence & Business Analytics Platform

An end-to-end **Customer Intelligence and Business Analytics Platform** that combines **Data Analytics, RFM Customer Segmentation, Machine Learning, FastAPI, React, MySQL/MariaDB, and Power BI**.

The platform helps businesses understand customer behavior, identify valuable and at-risk customers, analyze revenue, and support customer retention decisions.

---

# 📌 Project Overview

| Item | Description |
|---|---|
| Project Name | Customer Intelligence & Business Analytics Platform |
| Domain | Data Analytics + Machine Learning + Business Intelligence |
| Frontend | React.js + Vite |
| Backend | FastAPI + Python |
| Database | MySQL / MariaDB |
| Machine Learning | Logistic Regression |
| Customer Analysis | RFM Segmentation |
| Visualization | React + Recharts + Power BI |
| API | REST API |
| Version Control | Git + GitHub |

---

# 🎯 Objectives

| # | Objective |
|---:|---|
| 1 | Analyze customer purchasing behavior |
| 2 | Identify high-value customers |
| 3 | Segment customers using RFM analysis |
| 4 | Predict customers likely to churn |
| 5 | Identify high-risk customers |
| 6 | Analyze revenue and sales trends |
| 7 | Analyze product and category performance |
| 8 | Analyze country-wise business performance |
| 9 | Provide REST APIs for analytics |
| 10 | Build interactive dashboards |

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────────┐
                         │      React Frontend     │
                         │  Interactive Dashboard  │
                         └────────────┬────────────┘
                                      │
                                      │ REST API
                                      ▼
                         ┌─────────────────────────┐
                         │     FastAPI Backend     │
                         │     Analytics APIs      │
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
          │    RFM Analysis     │             │  Churn Prediction   │
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
                           │ Business Intelligence   │
                           │       Dashboard         │
                           └─────────────────────────┘
```

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 📊 Business Analytics | Analyze revenue, orders, customers and products |
| 👥 RFM Segmentation | Classify customers based on purchasing behavior |
| 🤖 Churn Prediction | Predict customers likely to stop purchasing |
| ⚠️ Risk Classification | Categorize customers into High, Medium and Low risk |
| 📈 Revenue Analysis | Analyze monthly revenue trends |
| 🛍️ Product Analysis | Identify top-performing products |
| 🏷️ Category Analysis | Compare product category performance |
| 🌍 Country Analysis | Compare revenue and customers by country |
| 📊 Power BI | Interactive business intelligence dashboard |
| 🖥️ React Dashboard | Interactive web-based analytics dashboard |
| 🔌 REST APIs | FastAPI endpoints for analytics |
| 📥 CSV Export | Export customer and churn information |

---

# 👥 RFM Customer Segmentation

RFM stands for:

| Metric | Meaning | What it Measures |
|---|---|---|
| **Recency** | How recently | Days since the customer's last purchase |
| **Frequency** | How often | Number of orders made by the customer |
| **Monetary** | How much | Total amount spent by the customer |

### Customer Segments

| Segment | Meaning |
|---|---|
| 🏆 Champions | Highly valuable and highly engaged customers |
| 💙 Loyal Customers | Customers who purchase frequently |
| 🌱 Potential Loyalists | Customers with potential to become loyal |
| 🆕 New Customers | Recently acquired customers |
| ⚠️ At Risk | Customers showing reduced engagement |
| 🔴 Lost Customers | Customers with low recent engagement and purchasing activity |

---

# 🤖 Customer Churn Prediction

The Machine Learning component predicts whether customers are likely to churn.

### Features

| Feature | Description |
|---|---|
| Recency | Days since last purchase |
| Frequency | Number of previous orders |
| Monetary | Total customer spending |
| Average Order Value | Average amount spent per order |

### Machine Learning Model

| Component | Technology |
|---|---|
| Data Processing | Pandas + NumPy |
| Feature Scaling | StandardScaler |
| Algorithm | Logistic Regression |
| Train/Test Split | 80/20 |
| Prediction | Churn Probability |
| Model Storage | Joblib |

### ML Pipeline

```text
Customer Transaction Data
          │
          ▼
Feature Engineering
          │
          ▼
Recency + Frequency + Monetary + AOV
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
```

---

# ⚠️ Churn Risk Classification

| Churn Probability | Risk Level | Business Meaning |
|---:|---|---|
| ≥ 70% | 🔴 High Risk | Customer requires immediate attention |
| ≥ 40% | 🟠 Medium Risk | Customer may require engagement |
| < 40% | 🟢 Low Risk | Lower churn probability |

---

# 📈 Power BI Dashboard

The Power BI dashboard provides a business-level view of the data.

| Dashboard Section | Information |
|---|---|
| KPI Cards | Customers, Orders, Revenue, AOV |
| Revenue Analysis | Monthly revenue trends |
| RFM Analysis | Customer segment distribution |
| Product Analysis | Product revenue and units sold |
| Category Analysis | Category performance |
| Churn Analysis | Churn risk and revenue at risk |
| Customer Analysis | High-risk and top customers |
| Country Analysis | Country-wise revenue and customers |

---

# 🖥️ React Dashboard

| Component | Purpose |
|---|---|
| KPI Cards | Display important business metrics |
| Revenue Chart | Show monthly revenue |
| RFM Chart | Display customer segments |
| Category Chart | Compare category revenue |
| Customer Table | Display top customers |
| Product Table | Display top products |
| Churn Section | Analyze customer churn |
| Risk Table | Display high-risk customers |
| Country Section | Compare country performance |
| Business Insights | Highlight important findings |
| CSV Export | Download analytical data |
| Dark Mode | Improve dashboard usability |

---

# 🔌 REST API

The backend is built using **FastAPI**.

| Endpoint | Description |
|---|---|
| `/` | API status |
| `/health` | Health check |
| `/customers` | Customer data |
| `/analytics/kpis` | Business KPIs |
| `/analytics/revenue` | Monthly revenue |
| `/analytics/customers` | Top customers |
| `/analytics/segments` | RFM customer segments |
| `/analytics/products` | Top products |
| `/analytics/countries` | Country performance |
| `/analytics/categories` | Category performance |
| `/analytics/churn` | Churn analysis |
| `/analytics/churn/customers` | High-risk customers |

### API Documentation

FastAPI provides interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🗄️ Database Design

Database:

```text
customer_intelligence
```

| Table | Purpose |
|---|---|
| `customers` | Stores customer information |
| `products` | Stores product information |
| `orders` | Stores customer orders |
| `order_items` | Stores products inside each order |
| `customer_segments` | Stores RFM segmentation results |
| `churn_predictions` | Stores ML churn predictions |

### Main Relationships

```text
customers
    │
    │ 1 : Many
    ▼
orders
    │
    │ 1 : Many
    ▼
order_items
    │
    │ Many : 1
    ▼
products

customers
    │
    ├──────────────► customer_segments
    │
    └──────────────► churn_predictions
```

---

# 📊 Dataset

| Dataset Component | Count |
|---|---:|
| Customers | 1,000 |
| Products | 100 |
| Orders | 5,000 |
| Product Categories | 5 |
| Countries | 6 |

### Product Categories

| # | Category |
|---:|---|
| 1 | Electronics |
| 2 | Clothing |
| 3 | Home |
| 4 | Beauty |
| 5 | Books |

### Countries

| # | Country |
|---:|---|
| 1 | India |
| 2 | USA |
| 3 | UK |
| 4 | Canada |
| 5 | Germany |
| 6 | Australia |

---

# 📈 Business Results

| Metric | Value |
|---|---:|
| Total Customers with Orders | **994** |
| Total Orders | **5,000** |
| Total Revenue | **7,361,180.78** |
| Average Order Value | **1,472.24** |

---

# 👥 RFM Segmentation Results

| Segment | Customers |
|---|---:|
| ⚠️ At Risk | **286** |
| 🆕 New Customers | **232** |
| 🌱 Potential Loyalists | **166** |
| 💙 Loyal Customers | **128** |
| 🔴 Lost Customers | **112** |
| 🏆 Champions | **70** |

### Key Insight

The **At Risk** segment contains the largest group of customers, making it an important segment for customer retention campaigns.

---

# 🤖 Churn Prediction Results

The churn model generated predictions for **1,000 customers**.

| Risk Category | Customers |
|---|---:|
| 🔴 High Risk | **380** |
| 🟠 Medium Risk | **620** |
| 🟢 Low Risk | **0** |

### Revenue by Risk Category

| Risk Category | Customer Monetary Value |
|---|---:|
| 🔴 High Risk | **1,097,768.86** |
| 🟠 Medium Risk | **5,029,820.42** |

---

# 🌍 Country Performance

| Country | Customers | Orders | Revenue |
|---|---:|---:|---:|
| Germany | 186 | 971 | 1,443,600.79 |
| Australia | 170 | 858 | 1,279,323.85 |
| UK | 170 | 883 | 1,273,399.06 |
| Canada | 164 | 801 | 1,210,285.08 |
| India | 161 | 792 | 1,165,400.43 |
| USA | 143 | 695 | 1,011,116.52 |

---

# 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React.js, Vite, Axios, Recharts, Lucide React |
| Backend | Python, FastAPI, SQLAlchemy, PyMySQL |
| Database | MySQL / MariaDB |
| Data Analysis | Pandas, NumPy, SQL |
| Machine Learning | Scikit-learn, Logistic Regression, StandardScaler |
| Model Storage | Joblib |
| Visualization | Recharts, Power BI |
| Version Control | Git, GitHub |
| Development | VS Code |
| Local Server | XAMPP |

---

# 📂 Project Structure

```text
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
```

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/himashrik/customer-intelligence-platform.git
cd customer-intelligence-platform
```

---

## 2. Database Setup

Start MySQL/MariaDB.

Create the database:

```sql
CREATE DATABASE customer_intelligence;
USE customer_intelligence;
```

Create the required tables using the SQL scripts inside:

```text
sql/
```

---

## 3. Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 4. Configure Database

Create:

```text
backend/.env
```

Add:

```env
DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/customer_intelligence
```

> Never commit `.env` files containing passwords, API keys, or other secrets.

---

## 5. Start FastAPI

From the `backend` directory:

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 6. Load Dataset

Navigate to:

```bash
cd ../data
```

Generate data:

```bash
python generate_data.py
```

Validate data:

```bash
python validate_data.py
```

Load data:

```bash
python load_data.py
```

---

## 7. Run Churn Prediction

Navigate to:

```bash
cd ../ml
```

Run:

```bash
python churn_prediction.py
```

This generates:

```text
churn_predictions.csv
churn_model.pkl
```

Load predictions into the database:

```bash
python load_churn.py
```

---

## 8. Start React Frontend

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🔄 Complete Data Flow

```text
                    CSV Dataset
                         │
                         ▼
                  Data Validation
                         │
                         ▼
                  MySQL / MariaDB
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
       RFM Analysis           ML Churn Model
             │                       │
             ▼                       ▼
      Customer Segments       Churn Predictions
             │                       │
             └───────────┬───────────┘
                         ▼
                   FastAPI Backend
                         │
                         ▼
                  React Dashboard
                         │
                         ▼
                     Power BI
```

---

# 💡 Business Use Cases

| Use Case | How the Platform Helps |
|---|---|
| Customer Retention | Identify customers at risk of churn |
| Customer Segmentation | Create targeted campaigns |
| Revenue Analysis | Track revenue performance |
| Product Optimization | Identify high-performing products |
| Category Analysis | Compare product categories |
| Geographic Analysis | Compare countries |
| Customer Value | Identify high-value customers |
| Marketing | Target specific customer segments |
| Business Intelligence | Support data-driven decisions |

---

# 🎯 Future Enhancements

| Enhancement | Description |
|---|---|
| Real-time Analytics | Process live customer transactions |
| Advanced Churn Models | Compare Random Forest and XGBoost |
| CLV Prediction | Predict Customer Lifetime Value |
| Retention Recommendations | Automatically recommend retention actions |
| Email Integration | Send customer retention campaigns |
| Authentication | Add role-based login |
| Cloud Deployment | Deploy the application to the cloud |
| Model Retraining | Automatically retrain the ML model |
| Advanced Power BI | Add more business intelligence reports |
| Real-time Pipelines | Build streaming data pipelines |

---

# 🔒 Security

The project follows basic security practices:

| Practice | Purpose |
|---|---|
| Environment Variables | Store database configuration |
| `.gitignore` | Prevent sensitive files from being committed |
| API Separation | Separate frontend and backend |
| SQLAlchemy | Structured database access |
| No Credentials in GitHub | Protect passwords and API keys |

**Never commit passwords, API keys, or `.env` files to GitHub.**

---

# 📌 Project Highlights

This project demonstrates practical knowledge of:

| Area | Skills Demonstrated |
|---|---|
| Full Stack | React + FastAPI |
| Backend | REST API development |
| Database | MySQL / MariaDB |
| SQL | Analytics and RFM queries |
| Data Analysis | Pandas + NumPy |
| Machine Learning | Logistic Regression |
| Customer Analytics | RFM Segmentation |
| Churn Analytics | Risk prediction |
| Visualization | Recharts + Power BI |
| Business Intelligence | KPI and dashboard development |
| Version Control | Git + GitHub |

---

# 👩‍💻 Author

## Himashri Kandi

**B.Tech – Information Technology**

GitHub:  
https://github.com/himashrik

---

# ⭐ Acknowledgement

This project was developed as a practical implementation of:

**Data Analytics + Machine Learning + Full-Stack Development + Business Intelligence**

---

## ⭐ If you found this project useful, consider giving it a star!
