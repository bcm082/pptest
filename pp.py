# Create a simple streamlit app to display the data
import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv('./105.csv')

# Create a title
st.title('CBO 105th Congressional')

# Display the data as a table
st.dataframe(df)
