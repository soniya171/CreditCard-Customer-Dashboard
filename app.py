import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit layout
st.set_page_config(page_title="Credit Card Dashboard", layout="wide")

# Load the dataset
try:
    df = pd.read_csv("data/BankChurners.csv")
    st.success("✅ Dataset loaded successfully!")
except Exception as e:
    st.error(f"❌ Failed to load dataset: {e}")
    st.stop()

# Display first few rows to confirm it's loading
st.write("### 👀 Data Preview (First 5 rows):")
st.write(df.head())

# Drop unnecessary unnamed columns if they exist
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Rename columns for dashboard use
df.rename(columns={
    'CLIENTNUM': 'CustomerID',
    'Customer_Age': 'Age',
    'Gender': 'Gender',
    'Education_Level': 'Education',
    'Marital_Status': 'Marital_Status',
    'Income_Category': 'Income',
    'Card_Category': 'Card_Type',
    'Months_on_book': 'Tenure',
    'Credit_Limit': 'Credit_Limit',
    'Total_Revolving_Bal': 'Outstanding_Balance',
    'Total_Trans_Ct': 'Total_Transactions',
    'Avg_Utilization_Ratio': 'Avg_Utilization_Ratio',
    'Attrition_Flag': 'Churn_Status'
}, inplace=True)

# Add binary churn risk for visualization
if 'Churn_Status' in df.columns:
    df['Churn_Risk'] = df['Churn_Status'].apply(lambda x: 1 if 'Attrited' in x else 0)
else:
    st.warning("⚠️ 'Churn_Status' column not found. Skipping churn risk metrics.")
    df['Churn_Risk'] = 0

# Sidebar filters
st.sidebar.header("🔍 Filter Customers")
gender = st.sidebar.multiselect("Select Gender", df['Gender'].unique())
education = st.sidebar.multiselect("Select Education Level", df['Education'].unique())
card_type = st.sidebar.multiselect("Select Card Type", df['Card_Type'].unique())

filtered_df = df.copy()
if gender:
    filtered_df = filtered_df[filtered_df['Gender'].isin(gender)]
if education:
    filtered_df = filtered_df[filtered_df['Education'].isin(education)]
if card_type:
    filtered_df = filtered_df[filtered_df['Card_Type'].isin(card_type)]

# KPIs
st.markdown("### 📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(filtered_df))

# Safe calculation of metrics
try:
    col2.metric("Avg Credit Limit", f"${filtered_df['Credit_Limit'].mean():,.2f}")
except:
    col2.metric("Avg Credit Limit", "N/A")

try:
    churn_rate = filtered_df['Churn_Risk'].mean() * 100
    col3.metric("Churn Rate", f"{churn_rate:.2f}%")
except:
    col3.metric("Churn Rate", "N/A")

# Utilization Ratio Histogram
if 'Avg_Utilization_Ratio' in filtered_df.columns:
    st.markdown("### 📈 Credit Utilization Ratio")
    fig1 = px.histogram(filtered_df, x="Avg_Utilization_Ratio", nbins=20, color="Gender")
    st.plotly_chart(fig1, use_container_width=True)

# Transactions vs Outstanding Balance
if 'Total_Transactions' in filtered_df.columns and 'Outstanding_Balance' in filtered_df.columns:
    st.markdown("### 💳 Transactions vs Balance")
    fig2 = px.scatter(
        filtered_df,
        x="Total_Transactions",
        y="Outstanding_Balance",
        size="Credit_Limit" if "Credit_Limit" in filtered_df.columns else None,
        color="Churn_Status" if "Churn_Status" in filtered_df.columns else None,
        hover_data=["CustomerID"]
    )
    st.plotly_chart(fig2, use_container_width=True)

# Top customers table
st.markdown("### 🏆 Top 10 Customers by Credit Limit")
if "Credit_Limit" in filtered_df.columns:
    top_customers = filtered_df.sort_values(by="Credit_Limit", ascending=False).head(10)
    st.dataframe(top_customers[[
        "CustomerID", "Credit_Limit", "Outstanding_Balance", "Total_Transactions", "Churn_Status"
    ]])
else:
    st.warning("⚠️ 'Credit_Limit' column not found. Cannot show top customers.")
