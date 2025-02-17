import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)

# Clear previous output
st.empty()  # This will clear the previous output

# Read data from Google Sheets
sheets_data = conn.read(worksheet=None)  # Read all sheets

# If multiple sheets, select the sheet by name (or specify another sheet name)
if isinstance(sheets_data, dict):
    sheet_name = "reports"  # Replace with the actual sheet name you want to select
    if sheet_name in sheets_data:
        df = sheets_data[sheet_name]
    else:
        st.error(f"Sheet '{sheet_name}' not found in the provided Google Sheets.")
        df = pd.DataFrame()  # Empty DataFrame in case of error
else:
    df = sheets_data  # Only one sheet

# Ensure correct column names
st.write("Columns in DataFrame:", df.columns.tolist())

# Check if 'Title' and 'Link' columns exist
required_columns = {"Title", "Link"}
if required_columns.issubset(df.columns):
    for index, row in df.iterrows():  # index is the row index, row is a Pandas Series
        st.write(f"{row['Title']} has a link: {row['Link']}")  # Access columns correctly
else:
    st.error("Error: 'Title' and 'Link' columns not found in the selected sheet.")
