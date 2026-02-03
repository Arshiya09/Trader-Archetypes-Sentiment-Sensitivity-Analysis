import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Page Config ---
st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("🎯 The Greed Trap: Trader Behavioral Insights")

# --- 1. Data Loading ---
# We use a function with a decorator to cache data so it loads fast
@st.cache_data
def load_data():
    # This checks both the root and the subfolder where you currently have it
    paths = ['cleaned_data.csv', 'trader-sentiment-analysis/notebooks/cleaned_data.csv']
    for path in paths:
        if os.path.exists(path):
            return pd.read_csv(path)
    return None

df = load_data()

if df is not None:
    # --- Sidebar Filters ---
    st.sidebar.header("Filter Results")
    sentiment = st.sidebar.multiselect("Select Sentiment", 
                                       options=df['classification'].unique(), 
                                       default=df['classification'].unique())
    
    filtered_df = df[df['classification'].isin(sentiment)]

    # --- 2. Key Metrics Row ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Trades", len(filtered_df))
    col2.metric("Avg. Win Rate", f"{(filtered_df['is_win'].mean() * 100):.1f}%")
    col3.metric("Avg. Trade Size", f"${filtered_df['Size USD'].mean():.2f}")

    # --- 3. Charts Section ---
    st.divider()
    
    left_chart, right_chart = st.columns(2)

    with left_chart:
        st.subheader("PnL Distribution by Sentiment")
        fig_pnl = px.box(filtered_df, x="classification", y="Closed PnL", 
                         color="classification", points="all",
                         color_discrete_map={'Fear': '#EF553B', 'Greed': '#00CC96'})
        st.plotly_chart(fig_pnl, use_container_width=True)

    with right_chart:
        st.subheader("Trade Size vs. Sentiment")
        fig_size = px.violin(filtered_df, x="classification", y="Size USD", 
                             box=True, color="classification",
                             color_discrete_map={'Fear': '#EF553B', 'Greed': '#00CC96'})
        st.plotly_chart(fig_size, use_container_width=True)

else:
    st.error("🚨 'cleaned_data.csv' not found! Please run your Jupyter Notebook first to save the cleaned data.")
    st.info("In your notebook, add this line at the end: `df.to_csv('cleaned_data.csv', index=False)`")