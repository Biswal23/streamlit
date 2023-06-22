import streamlit as st
from datetime import date
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
import math

from yfinance import ticker

st.title('Stock Dashboard')
start_date = st.sidebar.text_input('Start Date')
end_date = st.sidebar.date('End Date')

import yfinance as yf
import pandas as pd

# Define the list of ticker symbols for all stocks
all_ticker_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "FB", ...]  # Add all the ticker symbols

# Define the initial investment amount
initial_investment = 100000  # Adjust the amount as per your preference

# Define the number of top performing stocks to select
num_top_stocks = 10  # Adjust the number of stocks as per your preference

# Fetch historical data for all stocks till one day prior to the investment day
start_date = "2022-01-01"  # Adjust the start date as per your preference
end_date = "2022-12-30"  # Adjust the end date as per your preference

data = yf.download(all_ticker_symbols, start=start_date, end=end_date)

# Calculate the performance of each stock in terms of percentage returns over the latest 100 days
last_day_prices = data['Adj Close'].iloc[-1]
past_100th_day_prices = data['Adj Close'].iloc[-101]

returns = (last_day_prices / past_100th_day_prices) - 1

# Select the top performing stocks
top_stocks = returns.nlargest(num_top_stocks)

# Get the ticker symbols of the top performing stocks
selected_ticker_symbols = top_stocks.index.tolist()

# Fetch historical data for selected stocks from the investment day till the end
selected_data = yf.download(selected_ticker_symbols, start=end_date, end=end_date)

# Extract adjusted close prices from the selected data
adj_close = selected_data['Adj Close']

# Calculate the number of shares to buy for each stock
num_shares = initial_investment / num_top_stocks / adj_close.iloc[0]

# Calculate the portfolio value for each day
portfolio_value = (adj_close * num_shares).sum(axis=1)

# Plot the portfolio equity curve
portfolio_value.plot(title='Benchmark Portfolio Equity Curve')

