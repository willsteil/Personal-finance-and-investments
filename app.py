# Personal Finance + Stock Recommendation App (Streamlit)
# Save this as app.py

import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="Finance Tracker + Stock Helper", page_icon="💰")

st.title("Personal Finance Tracker + Stock Helper")

# ----------------------
# EXPENSE TRACKER
# ----------------------
st.header("📊 Track Your Finances")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Type", "Amount", "Category"])

# Input fields
type_choice = st.selectbox("Type", ["Income", "Expense"])
amount = st.number_input("Amount ($)", min_value=0.0)
category = st.text_input("Category (e.g., Food, Rent, Salary)")

if st.button("Add Entry"):
    new_row = pd.DataFrame([[type_choice, amount, category]], columns=["Type", "Amount", "Category"])
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
    st.success("Entry added!")

# Display data
st.subheader("Your Transactions")
st.dataframe(st.session_state.data)

# Summary
income = st.session_state.data[st.session_state.data["Type"] == "Income"]["Amount"].sum()
expenses = st.session_state.data[st.session_state.data["Type"] == "Expense"]["Amount"].sum()
balance = income - expenses

st.write(f"**Total Income:** ${income:.2f}")
st.write(f"**Total Expenses:** ${expenses:.2f}")
st.write(f"**Balance:** ${balance:.2f}")

# ----------------------
# STOCK HELPER
# ----------------------
st.header("📈 Stock Helper")

st.write("This tool gives simple stock suggestions based on basic metrics.")

# User input
risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

# Simple stock suggestions (educational, not financial advice)
if risk == "Low":
    suggestions = ["AAPL", "MSFT", "JNJ"]
elif risk == "Medium":
    suggestions = ["GOOGL", "AMZN", "SPY"]
else:
    suggestions = ["TSLA", "NVDA", "ARKK"]

st.write("Suggested Stocks:", suggestions)

# Show stock data
selected_stock = st.selectbox("View Stock Data", suggestions)

if st.button("Get Stock Info"):
    stock = yf.Ticker(selected_stock)
    hist = stock.history(period="1mo")

    st.subheader(f"{selected_stock} - Last Month Performance")
    st.line_chart(hist["Close"])

    info = stock.info
    st.write("**Company:**", info.get("longName", "N/A"))
    st.write("**Sector:**", info.get("sector", "N/A"))
    st.write("**Market Cap:**", info.get("marketCap", "N/A"))

st.warning("⚠️ This is not financial advice. Always do your own research before investing.")


