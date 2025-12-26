import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PCA Manufacturing Analytics Dashboard",
    layout="wide"
)

st.title("PCA-Based Manufacturing Analytics Dashboard for a Realtime Automated Filling Line")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Data Explorer", "PCA Insights"])

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_data.csv")

df = load_data()

if page == "Overview":
    st.header("Project Overview")
    st.markdown("""
    This dashboard visualises PCA insights from a realtime automated filling line.
    It supports variability analysis, anomaly detection, and continuous improvement.
    """)

elif page == "Data Explorer":
    st.header("Data Explorer")
    st.dataframe(df)

elif page == "PCA Insights":
    st.header("PCA Insights")
    st.write("This section will show PCA scores, loadings, and explained variance.")
