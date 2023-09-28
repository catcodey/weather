import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
st.title("My Streamlit App")

df=pd.read_csv("air-quality-india.csv")
st.write(df)
# List of required libraries


