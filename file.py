import streamlit as st 
import pandas as pd

df=pd.read_csv("election_final.csv")

st.title("Basic illustration of Scraping a data using selenium")

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])


tab1.subheader("A tab with a chart")
tab1.line_chart(df,x='State',y='seats_won')

tab2.subheader("A tab with the data")
tab2.write(df)