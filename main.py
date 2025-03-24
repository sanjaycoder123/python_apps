import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg",width=400)

with col2:
    st.title('Python Portfolio')
    content1 = """
    Hi, I'm Sanjay Bhattacharjee

I am a passionate software developer with a deep expertise in full-stack development. My focus is on building scalable and high-performance web applications using modern technologies like React, Node.js, and Python.

I’m always eager to learn, adapt, and grow in the ever-evolving tech landscape. Whether it’s optimizing front-end experiences or developing powerful back-end systems, I take pride in creating seamless, user-friendly, and reliable applications.
    """
    st.info(content1)
content2 = """
below you can check my apps if you want ,Thanks you!    
"""
st.write(content2)

col3,col4 = st.columns(2)

df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[10:].iterrows():
        st.header(row['title'])

with col4:
    for index,row in df[:10].iterrows():
        st.header(row['title'])



