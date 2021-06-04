#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 

# Markdown
#st.markdown("## Streamlit  ")
# Adding A Link
#url_link = "https://icfoss.in/"
#st.markdown(url_link)

#st.markdown("[Google](https://google.com)")


#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Titanic_Dataset")

#import dataset
df = pd.read_csv('titanic.csv')
#First thirty rows
titanic = df.head(10)


#Display the table
st.table(titanic)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
titanic.plot(kind='bar')
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(titanic['Sex'])
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='Sex',y='Age',data=titanic,kind='scatter')
st.pyplot()
#pairplot
st.subheader("Pairplot")
sns.pairplot(titanic,hue='Sex',palette='rainbow')
st.pyplot()
#Rugplot
st.subheader("Rugplot")
sns.rugplot(titanic['Age'])
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(titanic.corr(),cmap='coolwarm',annot=True)
st.pyplot()

#arr = np.random.normal(1, 1, size=100)
 
#st.(arr)


#data = np.random.randn(10, 2)
#st.table(data)

# Show the data as a chart.
#chart = st.line_chart(data)


n=np.arange(2,22,2)
st.write("DataFrame of numbers with starting value is 2 and end point is 22  with 2 steps")
st.dataframe(n)
st.write('Mean of above table is:' , n.mean())

st.write("visualization of table with 'Area_chart' ")
chart = st.area_chart(n) 

#SIDE Bar
st.sidebar.header("Parminderjeet kaur")
st.sidebar.text("Student")
#st.sidebar.text(url_link)
#st.sidebar.text("[Google](https://google.com)")

