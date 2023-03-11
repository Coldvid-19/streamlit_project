import math
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import requests as requests
import datetime
from alpha_vantage.timeseries import TimeSeries

api_key = 'FU7G5GQKP96N4PJV'

st.set_page_config(page_title="MyFirstStreamlitPage", layout="wide")

st.subheader("Hi, I am Nicholas Yeong.")
st.title("This is a tutorial for streamlit")

# Get a list of all available tickers
all_tickers = yf.Tickers("")

#Settings
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
time_series = ('WEEKLY', 'WEEKLY_ADJUSTED', 'MONTHLY', 'MONTHLY_ADJUSTED')

#selection boxes
selected_ticker = st.selectbox('Select a ticker', stocks)
selected_timeSeries = st.selectbox('Select time series', time_series)
start_date = st.date_input("Start date", (datetime.date(2013, 1, 1)))
end_date = st.date_input("End date", datetime.date.today())

startDate = (start_date.strftime("%Y-%m-%d"))
endDate = (end_date.strftime("%Y-%m-%d"))

# Alpha Vantage API call
# info_url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={selected_ticker}&apikey={api_key}'
# info_r = requests.get(info_url)
# info_data = info_r.json()
# company_name = info_data['Name']
# description = info_data['Description']
# company_country = info_data['Country']

st.subheader('Company Overview')

# st.write(f'Company : {company_name}')
# st.write(description)
# st.write(f'Country : {company_country}')

st.subheader('Historical Records')

historicalData_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{selected_timeSeries}&symbol={selected_ticker}&apikey={api_key}'
historicalData_r = requests.get(historicalData_url)
historicalData = historicalData_r.json()
key = list(historicalData.keys())[1]
processedData = historicalData[key]
filteredData = pd.DataFrame({date: values for date, values in processedData.items() if startDate <= date <= endDate}).T

st.write(filteredData)

