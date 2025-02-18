# src/data/data_loader.py
import pandas as pd
import streamlit as st

class DataLoader:
    def __init__(self):
        # Initialize the Google Sheets connection
        self.conn = st.connection("gsheets", type=st.secrets.connections.gsheets)
        
    @st.cache_data(ttl=3600)  # Cache data for 1 hour
    def load_sheet_data(self, sheet_name: str) -> pd.DataFrame:
        """Load data from specified Google Sheet with caching."""
        try:
            df = self.conn.read(worksheet=sheet_name)
            return df
        except Exception as e:
            st.error(f"Error loading sheet '{sheet_name}': {str(e)}")
            return pd.DataFrame()  # Return empty DataFrame on error