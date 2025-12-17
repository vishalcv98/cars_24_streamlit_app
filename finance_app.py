import yfinance as yf #yahoofinance
import streamlit as st

st.title("Stock Dashboard")

tab1, tab2, tab3 = st.tabs(["Overview", "Price Chart", "Volume"])

comp = st.text_input("Enter stock ticker", "AAPL").upper()
df = yf.Ticker(comp).history(start="2019-01-01", end="2023-01-01")

with tab1:
    st.subheader("Raw Data")
    st.dataframe(df)

with tab2:
    st.subheader("Closing Price")
    st.line_chart(df["Close"])

with tab3:
    st.subheader("Trading Volume")
    st.bar_chart(df["Volume"])