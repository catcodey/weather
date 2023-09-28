import streamlit as st
from streamlit_option_menu import option_menu
st.title( " EDA ")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import io


with st.sidebar:
  selected=option_menu(
    menu_title=None,
    options=["overview","how aqi varies with time","highest and lowest aqi analysis"],
    default_index=0)
  

df=pd.read_csv("air-quality-india.csv")
df.rename(columns = {'PM2.5':'aqi'}, inplace = True)

################## OVERVIEW TAB ###################

if selected=="overview":   #overview tab
  
  st.write(df)   #dataframe displayed
  col1, col2, col3 = st.columns(3)

  with col1:  #for displaying buttn=ons side by side. this is for show info
    a=st.button("show info")  #creating show info button
    
    if a: #if show info button is clciked then,

      buffer = io.StringIO()
      df.info(buf=buffer)  #storing  df.info values in buffer as its outputs to console not web pg
      info= buffer.getvalue()
      st.text(info)  #displaying content of df.info

      #if st.button('Reset'):   #non conventional way
       #  a=False

  with col2:
    b=st.button("check null values")
    
    if b:
      mis=df.isnull().sum()
      st.write(mis)  #displaying content of mis
 
  with col3:
    c=st.button("describe")

    if c:  
      st.write(df.describe())

#ADDING RESET ALL BUTTON
  if a==True or b==True or c==True:
    if st.button("RESET ALL"):
      a=False
      b=False
      c=False

########## HOW AQI VAORES WITH TIME TAB#########

if selected=="how aqi varies with time":


  aqi_option = st.selectbox(
    "Select one of the comparisons below and the gragh will be displayed",
    ("Year vs aqi", "Month vs aqi", "Hour vs aqi"),
    index=None,
    placeholder="Select",
  )
  

  st.write('You selected:', aqi_option)
  a=sns.barplot(x='Year',y='aqi',data=df,estimator=np.std)
  st.write(a)
# List of required libraries


