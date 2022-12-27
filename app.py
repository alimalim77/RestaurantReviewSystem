import streamlit as st
import pandas as pd 

import plotly.express as px 

from PIL import Image

st.set_page_config(page_title="Customer Reviews")
st.header("Analyzed Customer Reviews")
st.subheader("Ratings from the customer")

excel_file = 'restaurant.xlsx'
excel_file2 = 'opinion.xlsx'
sheet = 'Sheet1'

df = pd.read_excel(excel_file,
sheet_name=sheet,
usecols='B:E',
header=0,)


opinion = pd.read_excel(excel_file2,
sheet_name=sheet,
usecols='A:C',
header=0,)
pie = px.pie(opinion,title="Reviews",values="ProfileName",names="Opinion")



st.dataframe(df)
st.plotly_chart(pie) 