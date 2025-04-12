import streamlit as st

st.title("Forex Scanner v1")

st.write("Welcome to your real-time Forex trading scanner!")
import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.title("Forex Scanner v1")
st.subheader("Real-time Forex Data")

# List of forex pairs (you can add more)
symbols = ['EURUSD=X', 'GBPUSD=X', 'USDJPY=X']

# Choose pair
symbol = st.selectbox("Select Forex Pair", symbols)

# Define time range
end = datetime.datetime.now()
start = end - datetime.timedelta(days=1)

# Get data
data = yf.download(symbol, start=start, end=end, interval='15m')

# Show data
st.line_chart(data['Close'])
st.dataframe(data.tail())
