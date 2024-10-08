import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
from sklearn.datasets import load_iris

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data = iris.data, columns= iris.feature_names)
    df['spices'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['spices'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider('Sepal length', float(df['sepal length (cm)'].min()) , float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider('Sepal width', float(df['sepal width (cm)'].min()) , float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider('Petal length', float(df['petal length (cm)'].min()) , float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider('Petal width', float(df['petal width (cm)'].min()) , float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)

st.write('prediction')
st.write(f'The predicted species is : {target_names[prediction][0]}')