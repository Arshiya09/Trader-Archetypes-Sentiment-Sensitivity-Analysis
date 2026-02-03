import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Trader Sentiment Analysis", layout="wide")

st.title("📊 Trader Behavioral Dashboard")
st.markdown("Exploring the impact of **Fear & Greed** on trader performance.")

# --- Sidebar Filters ---
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect("Select Sentiment", ["Fear", "Greed"], default=["Fear", "Greed"])

# --- Load Data (Replace with your cleaned df) ---
# df = pd.read_csv('cleaned_data.csv')

# --- Metric Row ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Trades", "1,240")
col2.metric("Avg. Win Rate", "54%", "2%")
col3.metric("Most Profitable Sentiment", "Greed")

# --- Visuals ---
st.subheader("PnL Distribution by Sentiment")
# fig = px.box(df, x="classification", y="Closed PnL", color="classification")
# st.plotly_chart(fig, use_container_width=True)