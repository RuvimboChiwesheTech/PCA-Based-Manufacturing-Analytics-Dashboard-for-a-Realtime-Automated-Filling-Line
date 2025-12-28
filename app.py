import streamlit as st
import pandas as pd
import json

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

# PAGE 1: OVERVIEW
if page == "Overview":
    st.header("Project Overview")
    st.markdown("""
    This dashboard visualises PCA insights from a realtime automated filling line.
    It supports variability analysis, anomaly detection, and continuous improvement.
    """)

# PAGE 2: DATA EXPLORER
elif page == "Data Explorer":
    st.header("Data Explorer")
    st.dataframe(df)

# PAGE 3: PCA INSIGHTS
elif page == "PCA Insights":
    st.header("PCA Insights")
    st.write("This section will show PCA scores, loadings, and explained variance.")

    # Load PCA results and limits
    pca_df = pd.read_csv("data/pca_results.csv")

    with open("data/limits.json", "r") as f:
        limits = json.load(f)

    T2_limit = limits["T2_limit"]
    Q_limit = limits["Q_limit"]

    # Sidebar filters
    st.sidebar.subheader("🔍 Filter PCA Data")

    part_ids = pca_df["Part_ID"].unique()
    selected_parts = st.sidebar.multiselect("Select Part ID(s):", part_ids, default=part_ids)

    if "Reject_Type" in pca_df.columns:
        reject_types = pca_df["Reject_Type"].dropna().unique()
        selected_rejects = st.sidebar.multiselect("Select Reject Type(s):", reject_types, default=reject_types)
    else:
        selected_rejects = None

    if "Timestamp" in pca_df.columns:
        pca_df["Timestamp"] = pd.to_datetime(pca_df["Timestamp"])
        min_date = pca_df["Timestamp"].min()
        max_date = pca_df["Timestamp"].max()
        selected_range = st.sidebar.slider("Select Timestamp Range:", min_date, max_date, (min_date, max_date))
    else:
        selected_range = None

    # Apply filters
    filtered_df = pca_df.copy()

    if selected_parts:
        filtered_df = filtered_df[filtered_df["Part_ID"].isin(selected_parts)]

    if selected_rejects is not None:
        filtered_df = filtered_df[filtered_df["Reject_Type"].isin(selected_rejects)]

    if selected_range is not None:
        filtered_df = filtered_df[
            (filtered_df["Timestamp"] >= selected_range[0]) &
            (filtered_df["Timestamp"] <= selected_range[1])
        ]

    # Preview filtered data
    st.write("Filtered PCA Data:")
    st.dataframe(filtered_df)



