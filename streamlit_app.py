
import streamlit as st
from streamlit_option_menu import option_menu
st.title( " EDA ")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import io
import subprocess

# List of required libraries
required_libraries = ["numpy", "pandas", "matplotlib","streamlit_option_menu"]

# Check if the required libraries are installed
missing_libraries = [lib for lib in required_libraries if not st.subprocess.call(['pip', 'show', lib]) == 0]

# Install missing libraries if any
if missing_libraries:
    st.write("Installing missing libraries...")
    for lib in missing_libraries:
        st.subprocess.call(['pip', 'install', lib])
    st.write("Libraries installed successfully!"
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
#checking for null values
'''df.isnull().sum()

#dropping timestamp column
df.drop('Timestamp',axis=1,inplace=True)
df'''


'''
#renaming aqi column
df.rename(columns = {'PM2.5':'aqi'}, inplace = True)
df

# **year vs aqi**









sns.pairplot(data=df)

df[df['Year']==2017]['aqi'].mean()

# **month vs aqi**

fig, ax = plt.subplots()
sns.barplot(x="Month",y="aqi",data=df)

# **hr vs aqi**

#w=df[df['Year']==a[0]]

sns.barplot(x='Hour',y='aqi',data=df)


st.pyplot(fig)






# **count of aqi for each year**
fig, ax = plt.subplots()
a=df.groupby("Year").count()["aqi"]
a.plot(kind="bar",xlabel="Year",ylabel="count", title="DataFrameGroupBy Plot")

st.pyplot(fig)

# **max recorded aqi for each year**

#max aqi of every year  #find the mean of all years.

a=df.groupby("Year")["aqi"].mean()
a.plot(kind="bar",xlabel="Year",ylabel="maximum recorded aqi",title="Maximum recorded aqi of each year")

#here we notice that the maximum recorded aqi was in 2017 and the minimum was recorded in the year 2020. lets check which month in 2017 recorded the hightest and lowest aqi.**

# **month that has max and min recorded aqi for 2017 along with the hourly analysis of aqi for 2017**

#first highest year highest month mean
import matplotlib.ticker as ticker
w=df[df["Year"]==2017].groupby("Month").mean()#gives max of every col of a month of the yr 2017

maxmonth=w.loc[w["aqi"].idxmax()] #gives year day hour corresponding to the overall max aqi. gives the month having max aqi
minmonth=w.loc[w["aqi"].idxmin()] #gives the month having min aqi
print("month having max aqi\n" ,maxmonth, "month having min aqi\n",minmonth,sep="\n")

st.header("hr vs aqi analysis for 2017")


month_time=df[df['Year']==2017].groupby('Hour').mean()

plt.figure(figsize=(10, 5))
g=sns.lineplot(x=month_time.index,y=month_time.aqi,data=month_time ,marker='o')
plt.title("aqi for the yr 2017(hourly analysis)")
g.xaxis.set_major_locator(ticker.MultipleLocator(1)) #define intervals in x axis(x axis scale)
g.set_xticks(range(24)) #(tick range)

g.xaxis.set_major_formatter(ticker.ScalarFormatter()) #to prevent this from getting displayedmatplotlib.axis.XTick at 0x7da52454b130>,<matplotlib.axis.XTick at 0x7da52454b220>


st.text("we find that the highest aqi in 2017 recorded was 97.71 in the month of November andlowest is 93.20 in the month of December.It is aloso intersting to note that the aqi is highest at around 5pm . This makes sense because...")

# **converting months to names**

#converting month nos to names
months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',12:'December'}


df["DOW"]= df["Month"].map(months_dict)
#df.drop("DOW",axis=1,inplace=True)



## **How aqi varies with time(hourly),month,year**

#mean aqi with time(hourly)
grped_hr=df.groupby("Hour").mean(numeric_only=True)
grped_hr_index=grped_hr.index
plt.figure(figsize=(8, 3))
#plt.subplot(1,2,1)
plt.plot(grped_hr_index, grped_hr.aqi, marker='o', color='red', linestyle='-')

plt.title('Mean AQI values with Time(Hour)')
plt.xlabel('Hour')
plt.ylabel('AQI')
plt.xticks(grped_hr_index) #??


# Streamlit app
st.title('Air Quality Analysis')


st.pyplot(fig)  # Display the plot in Streamlit

# You can add more Streamlit components to display results, such as text, tables, etc.


#mean aqi with month
grped_month=df.groupby("Month").mean(numeric_only=True)
grped_month_index=grped_month.index
plt.figure(figsize=(10,3))
plt.subplot(1,2,1)
plt.plot(grped_month_index, grped_month.aqi, marker='o', color='red', linestyle='-')
plt.title('Mean AQI values with Month')
plt.xlabel('Month')
plt.ylabel('AQI')


#mean aqi with year
grped_yr=df.groupby("Year").mean(numeric_only=True)
grped_yr_index=grped_yr.index
grped_month_index=grped_month.index
plt.subplot(1,2,2)
plt.plot(grped_yr_index, grped_yr.aqi, marker='o', color='red', linestyle='-')
plt.title('Mean AQI values with Year')
plt.xlabel('Year')
plt.ylabel('AQI')
st.pyplot(fig)
st.text("we can see that the aqi is generally very high between 5pm-7pm and also during 5am in the morning.The aqi gradually dips down after 7pm. (vehicular poll)")




st.header("Seasonal analysis")

st.text("we can see that between the months june to october there is a significant drop in aqi compared to its peak values in january and december")

st.header("weekend vs weekday")

p = df.groupby(df["Day"]%7==0).agg({"Day": "first", "aqi": "mean"})
i=df.groupby(~df["Day"].isin([5, 6])).agg({"Day": "first", "aqi": "mean"}) #weekday
print(p,i,sep="\n")



df[df["Day"]%7==0]["Day"].unique()

# **average air quality index for each month over the years**

monthly_avg_air_quality = df.groupby(['Year', 'Month'])['aqi'].mean()
a=pd.DataFrame(monthly_avg_air_quality)
a.head()
#a['Year']

# **converting above df to pivot table**

table = pd.pivot_table(a, values = 'aqi', index ='Year',
                         columns ='Month')
table

st.text("we notice that in the month of november theres a high aqi consistently because of festivals like diwaliDiwali is a Hindu festival that is celebrated with fireworks and bonfires. The burning of fireworks and bonfires releases large amounts of pollutants into the air.The poor air quality in India in November 2017 had a significant impact on public health. Schools were closed in Delhi and other cities due to the poor air quality. Many people also reported experiencing respiratory problems.The Indian government has taken a number of steps to address air pollution, including implementing stricter emission standards for vehicles and industries, and banning the burning of biomass. However, more needs to be done to improve air quality in Indiaes, there was a major restriction imposed after November 2017 to control air pollution in India. In January 2018, the Supreme Court of India banned the use of diesel vehicles older than 10 years in Delhi and the National Capital Region (NCR). The court also ordered the government to implement a number of other measures to reduce air pollution, including:")

st.text("Increasing the use of public transportationPromoting the use of electric vehiclesBanning the burning of biomassImplementing stricter emission standards for vehicles and industries")

# **highest aqi recorded along with the month and year** ::::

max_aqi=df['aqi'].max()#max aqi recorded
#which yr and month
df[(df['aqi']==max_aqi)][['Year','Month','aqi']]

#**the highest aqi recorded  was in the year 2018 in the month of novermber**





# **adding new col remark**

def remarkfn(x):
  if x>=0 and x<=50:
    return 'good'
  elif x>50 and x<=100:
    return 'satisfactory'
  elif x>100 and x<=200:
    return 'moderate'
  elif x>200 and x<=300:
    return 'poor'
  elif x>300 and x<=400:
    return 'very poor'
  elif x>400:
    return 'severe'
df['remark']=df['aqi'].apply(remarkfn)
df

# **barplot of year vs aqi with remark analysis of each year**


sns.barplot(x='Year',y='aqi',data=df,estimator=np.std,hue='remark')



st.text("we can see that aqi isnt very poor or severe during any of the years. The aqi is poorest in the year 2018 with the max no of poor recoded cases")





import pandas as pd



season_totals = df.groupby("Month")["aqi"].sum()
plt.figure(figsize=(8, 8))
plt.pie(season_totals, labels=season_totals.index, autopct="%1.1f%%", startangle=140)
plt.title("Air Quality Distribution by Season")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



summer = df[df["Month"].isin([3, 4, 5])]["aqi"].mean()
monsoon = df[df["Month"].isin([6, 7, 8, 9])]["aqi"].mean()
autumn = df[df["Month"].isin([10, 11])]["aqi"].mean()
winter = df[df["Month"].isin([12, 1])]["aqi"].mean()

st.header("seasonal analysis of aqi")

import pandas as pd
seasons = ['Summer', 'Monsoon', 'Autumn', 'Winter']
mean = [ summer,monsoon,autumn,winter]

plt.figure(figsize=(8, 8))
plt.pie(mean, labels=seasons, autopct="%1.1f%%", startangle=140)
plt.title("Air Quality Distribution by Seasons")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

"""theres a higher AIQ during winter and autumn months because of Weather Patterns: During winter and autumn, certain regions in India experience weather conditions that can contribute to poor air quality. For example, winter often brings temperature inversions, where cold air near the ground traps pollutants, leading to increased pollution levels. Reduced Dispersion: During winter, the lower temperatures and reduced wind speeds can limit the dispersion of pollutants, causing them to accumulate in the atmosphere and leading to higher AQI levels
"""
import seaborn as sns
import matplotlib.pyplot as plt


pivot_data = df.pivot_table(index='remark', columns='Month', values='aqi', aggfunc='mean')


plt.figure(figsize=(20,7))
sns.heatmap(pivot_data, cmap='YlGnBu', annot=True, fmt=".1f")
plt.title('Hourly and Daily AQI Levels')
plt.xlabel('Day of the Month')
plt.ylabel('Hour of the Day')
st.pyplot(fig)


df[(df['Hour']==18) & (df['remark']=='moderate')]['aqi'].mean()

df
st.header("seasonal analysis of aqi")

import pandas as pd
st.header("Air Quality Distribution by Seasons")
seasons = ['Summer', 'Monsoon', 'Autumn', 'Winter']
mean = [ summer,monsoon,autumn,winter]

b=plt.figure(figsize=(1.5, 1.5))
b.patch.set_facecolor('black')
plt.pie(mean, labels=seasons, autopct="%1.2f%%", startangle=140,textprops={"fontsize":4})
#plt.pie(mean, labels=seasons, autopct="%1.1f%%", startangle=140)
#plt.title("Air Quality Distribution by Seasons")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(b)

"""theres a higher AIQ during winter and autumn months because of Weather Patterns: During winter and autumn, certain regions in India experience weather conditions that can contribute to poor air quality. For example, winter often brings temperature inversions, where cold air near the ground traps pollutants, leading to increased pollution levels. Reduced Dispersion: During winter, the lower temperatures and reduced wind speeds can limit the dispersion of pollutants, causing them to accumulate in the atmosphere and leading to higher AQI levels
"""
import seaborn as sns
import matplotlib.pyplot as plt


pivot_data = df.pivot_table(index='remark', columns='Month', values='aqi', aggfunc='mean')


plt.figure(figsize=(20,7))
sns.heatmap(pivot_data, cmap='YlGnBu', annot=True, fmt=".1f")
plt.title('Hourly and Daily AQI Levels')
plt.xlabel('Day of the Month')
plt.ylabel('Hour of the Day')
st.pyplot(fig)


df[(df['Hour']==18) & (df['remark']=='moderate')]['aqi'].mean()



import pandas as pd
st.header("Air Quality Distribution by ratings")
poor_count=df[df['remark']=='poor']['Year'].count()
good_count=df[df['remark']=='good']['Year'].count()
moderate_count=df[df['remark']=='moderate']['Year'].count()
satisfactory_count=df[df['remark']=='satisfactory']['Year'].count()
poor_count,good_count,moderate_count,satisfactory_count
ratings = ['poor','good','satisfactory','moderate']
ratings_count= [ poor_count,good_count,moderate_count,satisfactory_count]

a=plt.figure(figsize=(1.5,1.5))
a.patch.set_facecolor('black')
plt.pie(ratings_count, labels=ratings, autopct="%1.2f%%", startangle=140,textprops={"fontsize":4})
#plt.figure(facecolor='salmon')
#plt.title("Air Quality Distribution by ratings",fontsize=20)
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(a)

'''
