import streamlit as st
import pandas as pd

st.title('My first Streamlit app')
st.write('Hello, Streamlit!')


option = st.sidebar.selectbox('Select one option:', ('Option 1', 'Option 2'))
st.write('You selected:', option)

df = pd.read_csv('data.csv')
# Convert date to datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Extract year and month
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month

st.dataframe(df)

dfone = df[["month", "Amount"]]
dftwo = dfone.groupby("month").mean()
st.bar_chart(dftwo)