import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl as op

# Set page configuration
st.set_page_config(page_title="Customer Reviews")

with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.header("Analyzed Customer Reviews")
st.subheader("Ratings from the customer")

excel_file = 'Reviews_Ans.xlsx'
excel_file2 = 'opinion.xlsx'
sheet = 'Sheet1'

# Takes the following total columns and presents them
st.header("Customer Information")
df = pd.read_excel(excel_file,
                   sheet_name=sheet,
                   usecols='A:C',
                   header=0,)

# Take the opinion excel file and generates a pie chart
st.subheader("Information on the reviews informations")
opinion = pd.read_excel(excel_file2,
                        sheet_name=sheet,
                        usecols='A:C',
                        header=0,)
workbook_op = op.load_workbook('opinion.xlsx')
sheet_op = workbook_op.active
good = sheet_op.cell(row=2, column=1).value
bad = sheet_op.cell(row=2, column=2).value


pie = px.pie(title="Reviews", values=[good, bad], names=["Good", "Bad"])
workbook_op.save('opinion.xlsx')

st.button("Send a message")
st.image("whatsapp.png", "Send a message to users", 100)

st.dataframe(df)
st.dataframe(opinion)
st.plotly_chart(pie)
