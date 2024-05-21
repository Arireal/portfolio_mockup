import streamlit as st
import pandas


st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Ariane Souza')
    content = """ Hi there, this is Ariane :)🚀 I am a passionate Python and Full Stack Developer. 
    I specialize in bringing projects to life through coding and solving complex UX/UI problems.
    From building robust web applications to enhancing user experiences, I love crafting elegant
    solutions that push the boundaries of technology and design. 
    🌟 Let's work together to turn your ideas into reality!"""
    st.write(content)

content2 = """ Below you can find some of the apps I have built in Python. Feel free to contact me!"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])





