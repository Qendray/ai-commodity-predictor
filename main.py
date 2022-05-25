import streamlit as st
from datetime import date
 
 import yfinance as yf
 from fbprophet import Prophet
 from fbprophet.plot import plot_plotly
from plotly import graph_objs as go


START = "2016-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("AI CPP")

commodities = ("CL=F","^N225","PL=F","HG=F","GC=F","BTI")
select_commodities = st.selectbox("Select dataset for predicion",commodities)

n_years = st.slider("Years of prediction",1,4)
period = n_years * 365