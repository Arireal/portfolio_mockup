import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Ariane Souza')
    content = """ Hi there, this is Alex:)🌺 I am a passionate graphic and brand designer. 
    I specialize in creating colorful and bold brands that truly stand out. From vibrant logos to eye-catching advertisements, 
    I love to play with colors and push the boundaries of traditional design. ✨Let's work together"""
    st.write(content)
