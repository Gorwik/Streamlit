import streamlit as st
import pandas as pd

data = {"Series1": [1, 2, 4, 5, 7], "Series2": [10, 30, 40, 100, 250]}
df = pd.DataFrame(data)

st.title("Our first streamlit App")
st.subheader("Introducing Streamlit in Automate Everything with Python")
st.write(
    """This is our first App.
Enjoy it
"""
)
st.write(df)
