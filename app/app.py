import streamlit as st
import pandas as pd
import json

# PAGE CONFIG
st.set_page_config(
    page_title="PCA Manufacturing Analytics Dashboard",
    layout="wide"
)

st.title("PCA-Based Manufacturing Analytics Dashboard for a Realtime Automated Filling Line")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Data Explorer", "PCA Insights"])

# LOAD CLEANED DATA
@st.cache_data
def load_cleaned_data():
    return pd.read_csv("data/processed/cleaned_data.csv")

df = load_cleaned_data()

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

    # Load PCA results
    pca_df = pd.read_csv("data/processed/pca_results.csv")

    # Load limits if available
    try:
        with open("data/limits.json", "r") as f:
            limits = json.load(f)
        T2_limit = limits.get("T2_limit", None)
        Q_limit = limits.get("Q_limit", None)
    except FileNotFoundError:
        T2_limit = None
        Q_limit = None

    # Sidebar filters
    st.sidebar.subheader("🔍 Filter PCA Data")

    # Part ID filter
    if "part_id" in pca_df.columns:
        part_ids = pca_df["part_id"].unique()
        selected_parts = st.sidebar.multiselect("Select Part ID(s):", part_ids, default=part_ids)
    else:
        selected_parts = None

    # Reject type filter
    if "reject_type" in pca_df.columns:
        reject_types = pca_df["reject_type"].dropna().unique()
        selected_rejects = st.sidebar.multiselect("Select Reject Type(s):", reject_types, default=reject_types)
    else:
        selected_rejects = None

    # Timestamp filter
    if "entry_timestamp" in pca_df.columns:
        pca_df["entry_timestamp"] = pd.to_datetime(pca_df["entry_timestamp"])
        min_date = pca_df["entry_timestamp"].min()
        max_date = pca_df["entry_timestamp"].max()
        selected_range = st.sidebar.slider("Select Timestamp Range:", min_date, max_date, (min_date, max_date))
    else:
        selected_range = None

    # Apply filters
    filtered_df = pca_df.copy()

    if selected_parts is not None:
        filtered_df = filtered_df[filtered_df["part_id"].isin(selected_parts)]

    if selected_rejects is not None:
        filtered_df = filtered_df[filtered_df["reject_type"].isin(selected_rejects)]

    if selected_range is not None:
        filtered_df = filtered_df[
            (filtered_df["entry_timestamp"] >= selected_range[0]) &
            (filtered_df["entry_timestamp"] <= selected_range[1])
        ]

    st.subheader("Filtered PCA Data")
    st.dataframe(filtered_df)

# KPI SECTION (ALWAYS SHOWN)
st.subheader("Key Performance Indicators")

pca_df = pd.read_csv("data/processed/pca_results.csv")

# Rename flags for consistency
pca_df.rename(columns={
    "T2_flag": "T2_Flag",
    "Q_flag": "Q_Flag"
}, inplace=True)

# Compute anomaly flag
pca_df["Anomaly"] = pca_df["T2_Flag"] | pca_df["Q_Flag"]

# KPI metrics
total_parts = len(pca_df)
total_anomalies = pca_df["Anomaly"].sum()
pct_anomalies = (total_anomalies / total_parts * 100) if total_parts > 0 else 0

# Most common reject type
if "reject_type" in pca_df.columns and pca_df["reject_type"].notna().any():
    top_reject = pca_df["reject_type"].mode()[0]
else:
    top_reject = "N/A"

# Display KPI tiles
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Parts", f"{total_parts}")
col2.metric("Total Anomalies", f"{total_anomalies}")
col3.metric("% Out of Control", f"{pct_anomalies:.2f}%")
col4.metric("Most Common Reject", top_reject)

