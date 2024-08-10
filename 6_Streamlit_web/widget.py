import streamlit as st
import pandas as pd
import numpy as np

name = st.text_input('Enter your name : ')
age = st.slider('age',0,100,25)


options = ['C', 'C++', 'Java', 'Python',"JavaScript"]
choice = st.selectbox('Language',options)
if name:
    st.write(f'hello {name}!')
st.write(f'age:  {age}')
st.write(f"You selected : {choice}")

df = pd.DataFrame({
    "Name":['shyam','sai','ram', 'krishna'],
    'Age':[34,32,12,23],
    'Marks':[98,78,98,89]
})

df.to_csv("data.csv")

uploaded_file = st.file_uploader("Choose the file",type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)