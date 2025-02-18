import streamlit as st
import sys
from pathlib import Path

# Add src to the Python path
src_dir = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from components.card import create_card
from data.data_loader import DataLoader

st.set_page_config(
    page_title="Data Catalog",
    page_icon="🏠",
    layout="wide"
)

st.title("Data Catalog")

st.markdown("""
Welcome to the Data Catalog! Here you'll find:
- Reports organized by division and KPI
- Data tools and utilities
- Training resources
- Support documentation
- Frequently asked questions
""")

try:
    # Display recent updates or featured content
    st.subheader("Featured Dashboards")
    loader = DataLoader()
    featured_reports = loader.load_sheet_data("Reports").head(3)

    for _, row in featured_reports.iterrows():
        create_card(
            title=row["Title"],
            description=row["Description"],
            link=row["Link"],
            key_metrics=row["Key Metrics"].split(","),
            support=row["Support"],
            tool=row["Tool"]
        )
except Exception as e:
    st.error(f"Error loading data: {str(e)}")