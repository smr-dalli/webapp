#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Start writing code here...
import streamlit as st
from PIL import Image
import pandas as pd

#Sidebar
logo = Image.open("logo.png")
st.sidebar.image(logo, width=100)
st.sidebar.header("Build Week 1")
st.sidebar.text("###Team:\nMarcin Szleszynski\nSaurabh Satasia\nSai Mohan Reddy Dalli")
st.sidebar.markdown("""### This is the website for [Streamlit](https://www.streamlit.io/) to publish the results from our first AI Build Week!""")

#Title
image = Image.open('minerva_mcgonagall_hero.jpg')
st.image(image)
st.title('Team McGonagall')
st.header('##Tasks for the Build Week 1')
st.text("""1. Webscraping the first 1000 Best Books listsof the Decade: 2000s from the [https://www.goodreads.com](https://www.goodreads.com/list/show/5.Best_Books_of_the_Decade_2000s) website.\n
2. Cleaning the dataset.\n
3. Calculating the Min max norm rating and Mean max norm rating.\n
4. Analysing the data and Visulaisation.""")
st.markdown("""### This is the README.md file [readme](https://github.com/martinezpl/goodreads_best2000/blob/main/README.md)""")

#dataset
df = pd.read_csv('Best_2000s.csv')
if st.button("Display the data."):
    st.dataframe(df)
st.markdown("""So much of data at once, can access individual columns here:""")
column = st.multiselect("Select the columns you want to display.",df.columns)
#st.markdown("Filter out the books under a thershold of number of awards:")
#threshold = st.slider('Filter out number of awards in between 200 to 800',2,40)
#filtered = df[df.awards_count >=threshold]
#st.dataframe(filtered[column])

