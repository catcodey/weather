import streamlit as st
import pandas as pd
df=pd.read_csv("air-quality-india.csv")
st.write(df)
