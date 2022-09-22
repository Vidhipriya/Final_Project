import streamlit as st 
from datetime import ate 
import yfinance as yf 
from fbprophet import prophet
from fbprophet.plot import plot_plotly 
from plotly import graph_obhs as go

start="2012-01-10"
today=date.today().strttime("%Y-%M-%d")


start = (datetime.date.today() - datetime.timedelta( NUM_DAYS ) )
end = datetime.datetime.today()


