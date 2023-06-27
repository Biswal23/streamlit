import streamlit as st
import pandas as pd


# Function to calculate portfolio equity curve
def calculate_equity_curve(initial_investment, stock_prices):
    num_stocks = len(stock_prices.columns)
    stock_weights = initial_investment / num_stocks
    portfolio_values = (stock_prices * stock_weights).sum(axis=1)
    equity_curve = portfolio_values.cumsum()
    return equity_curve


# Function to select top performing stocks based on past returns
def select_top_performing_stocks(stock_prices):
    returns = stock_prices.iloc[-1] / stock_prices.iloc[-101] - 1
    top_stocks = returns.nlargest(10)
    return top_stocks.index.tolist()


# Streamlit app
def main():
    st.title("Portfolio Equity Curve")
    st.write("This app calculates the portfolio equity curve based on past returns based selection strategy.")

    # Get user input for initial investment
    initial_investment = st.number_input("Initial Investment", min_value=1.0, step=1.0, value=10000.0)

    # Upload stock price data
    stock_prices = st.file_uploader("Upload CSV file with stock prices", type="csv")

    if stock_prices is not None:
        # Read stock price data
        df = pd.read_csv(stock_prices, index_col=0)

        # Select top performing stocks
        selected_stocks = select_top_performing_stocks(df)
        selected_prices = df[selected_stocks]

        # Calculate equity curve
        equity_curve = calculate_equity_curve(initial_investment, selected_prices)

        # Plot equity curve
        st.line_chart(equity_curve)


# Run the app
if __name__ == "__main__":
    main()
