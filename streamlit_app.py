import streamlit as st
import pandas as pd

import seaborn as sns

st.title("My Streamlit App")

df=pd.read_csv("air-quality-india")
st.write(df)
# List of required libraries


