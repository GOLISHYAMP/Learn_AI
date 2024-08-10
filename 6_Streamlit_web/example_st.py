import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello World!!!')
st.write('This is simple text')

df = pd.DataFrame({
    'firstCol':[10,20,30,40,50],
    'secondCol':[100,200,300,400,500]
}
)

st.write("here is the dataframe")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)

st.line_chart(chart_data)