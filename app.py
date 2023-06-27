import streamlit as st
import yfinance as fn
import pandas as pd

st.write(""" # My First App with Streamlit""")
st.title("Stock Market app with *Streamlit*")
st.header("Simple Data Science Web App")
st.sidebar.header("Menu \n Code Mark list")


#This is a function that fetches the company's ticker

def get_ticker(name):
    company = fn.ticker(name)
    return company

c1 = get_ticker ("RELIANCE")
c2 = get_ticker("HCLTECH")
c3 = get_ticker("TATAMOTORS")
c4 = get_ticker("M&M")
c5 = get_ticker("EICHERMOT")
c6 = get_ticker("JSWSTEE")
c7 = get_ticker("APOLLOHOSP")
c8 = get_ticker("WIPRO")
c9 = get_ticker("WIKI")
c10 = get_ticker("ADANIENT")

#fetching data for dataframe

reliance= fn.download("RELIANCE", start="2020-10-01", end="2022-11-01")
hcltech= fn.download("HCLTECH", start="2020-10-01", end="2022-11-01")
tatmotors= fn.download("TATAMOTORS", start="2020-10-01", end="2022-11-01")
m_m= fn.download("M&M", start="2020-10-01", end="2022-11-01")
eichermot= fn.download("EICHERMOT", start="2020-10-01", end="2022-11-01")
jswstee= fn.download("JSWSTEE", start="2020-10-01", end="2022-11-01")
apollohosp= fn.download("APOLLOHOSP", start="2020-10-01", end="2022-11-01")
wipro= fn.download("WIPRO", start="2020-10-01", end="2022-11-01")
wiki= fn.download("WIKI", start="2020-10-01", end="2022-11-01")
adanient= fn.download("ADANIENT", start="2020-10-01", end="2022-11-01")

#fetching historical data by valid periods ()
data1 = c1.history(period="3yr")
data2 = c2.history(period="3yr")
data3 = c3.history(period="3yr")
data4 = c4.history(period="3yr")
data5 = c5.history(period="3yr")
data6 = c6.history(period="3yr")
data7 = c7.history(period="3yr")
data8 = c8.history(period="3yr")
data9 = c9.history(period="3yr")
data10 = c10.history(period="3yr")


# Function to calculate portfolio equity curve
def calculate_equity_curve(initial_investment, stock_prices):
    num_stocks = len(stock_prices.columns)
    stock_weights = initial_investment / num_stocks
    portfolio_values = (stock_prices * stock_weights).sum(axis=1)
    equity_curve = portfolio_values.cumsum()
    return equity_curve


# Streamlit app
def main():
    st.title("Portfolio Equity Curve")
    st.write("This app calculates the portfolio equity curve based on an equal investment strategy.")

    # Get user input for initial investment
    initial_investment = st.number_input("Initial Investment", min_value=1.0, step=1.0, value=10000.0)

    # Upload stock price data
    stock_prices = st.file_uploader("Upload CSV file with stock prices", type="csv")

    if stock_prices is not None:
        # Read stock price data
        df = pd.read_csv(stock_prices, index_col=0)

        # Calculate equity curve
        equity_curve = calculate_equity_curve(initial_investment, df)

        # Plot equity curve
        st.line_chart(equity_curve)


# Run the app
if __name__ == "__main__":
    main()


