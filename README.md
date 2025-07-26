# 💳 Credit Card Customer Dashboard

An interactive dashboard built using **Streamlit** to analyze and visualize customer data from a credit card company. This project aims to uncover business insights such as churn risk, spending patterns, and customer segmentation using real-world data.

---

## 📁 Project Structure
CreditCard-Customer-Dashboard/
├── app.py # Streamlit dashboard code
├── data/
│ └── BankChurners.csv # Dataset
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🔍 Features

- 📊 Churn prediction insights and patterns  
- 🧠 Customer segmentation by education, card type, and income  
- 💳 Credit limit and transaction behavior analytics  
- 📌 Filterable and interactive charts for deeper insights  
- ⚡ KPI metrics to highlight important business indicators  

---

## 🧰 Tech Stack

- **Python**: Data processing & visualization  
- **Pandas**, **NumPy**: Data manipulation  
- **Plotly**: Interactive graphs and plots  
- **Streamlit**: Dashboard UI  
- **Dataset**: `BankChurners.csv` (Kaggle)

---

## 🚀 How to Run the Project

```bash
# 1. Clone the repository
git clone https://github.com/soniya171/CreditCard-Customer-Dashboard.git
cd CreditCard-Customer-Dashboard

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run app.py