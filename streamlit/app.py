import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Customer Reviews")

with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.header("Analyzed Customer Reviews")
st.subheader("Ratings from the customer")

excel_file = 'restaurant.xlsx'
excel_file2 = 'opinion.xlsx'
sheet = 'Sheet1'

st.header("Customer Information")
df = pd.read_excel(excel_file,
                   sheet_name=sheet,
                   usecols='B:E',
                   header=0,)

st.subheader("Information on the reviews informations")
opinion = pd.read_excel(excel_file2,
                        sheet_name=sheet,
                        usecols='A:C',
                        header=0,)
pie = px.pie(opinion, title="Reviews", values="ProfileName", names="Opinion")

st.button("Send a message")
st.image("whatsapp.png", "Send a message to users", 100)

st.dataframe(df)
st.plotly_chart(pie)
