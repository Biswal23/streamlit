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

data= yf.download(ticker,start = start_date, end=end_date)
fig = px.line(dstreamlitata, x=data.index, y=data['Adj Close'], title= ticker)
st.plotly_chart(fig)

pricing_data,fundamental_data = st.tabs(["Pricing Data","Fundamental Data"])

with pricing_data:
     st.header('Price Movement')
     data2 = data
     data2['% Change']= data['Adj Close'] / data['Adj Close'].shift(1)-1
     data2.dropna(inplace =True)
     st.write(data)
     annual_return = data2['% Change'].mean()*252*100
     st.write('Annual Return is', annual_return,'%')
     stdev= np.std(data2['% Change'])*np.sqrt(252)
     st.write('Standard Deviation is',stdev*100,'%')
