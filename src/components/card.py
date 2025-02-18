import streamlit as st

def create_card(title, description, link, key_metrics, support, tool):
    with st.container():
        st.markdown(f"""
        <div style="
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h3 style="margin-top: 0;">{title}</h3>
            <p>{description}</p>
            <p><strong>Key Metrics:</strong> {', '.join(metric.strip() for metric in key_metrics)}</p>
            <p><strong>Tool:</strong> {tool}</p>
            <p><strong>Support:</strong> {support}</p>
            <a href="{link}" target="_blank">View Report</a>
        </div>
        """, unsafe_allow_html=True)