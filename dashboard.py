import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Youtube Niche Analyzer", layout="wide")
st.title("Youtube Niche Analyzer")

keywords_df = pd.read_csv("analysis.csv")
channels_df = pd.read_csv("channel_analysis.csv")
time_df = pd.read_csv("time_analysis.csv")

st.header("Keyword Analysis")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        keywords_df.head(15),
        x="keyword",
        y="frequency",
        color="frequency",
        color_continuous_scale="blues",
        title="Most Common Keywords",
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(
        keywords_df.head(15),
        x="keyword",
        y="avg_views",
        color="avg_views",
        color_continuous_scale="reds",
        title="Keyword by Avg Views",
    )
    st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(
    keywords_df,
    x="frequency",
    y="avg_views",
    text="keyword",
    title="Keyword frequency vs Avg Views",
    labels={"frequency": "How often it appears", "avg_views": "Avg view count"},
)
fig3.update_traces(textposition="top center")
st.plotly_chart(fig3, use_container_width=True)

st.header("Channel Dominance")
col3, col4 = st.columns(2)

with col3:
    fig4 = px.bar(
        channels_df.head(10),
        x="channel",
        y="total_views",
        color="total_views",
        color_continuous_scale="greens",
        title="Top Channels by Total Views",
    )
    st.plotly_chart(fig4, use_container_width=True)

with col4:
    fig5 = px.bar(
        channels_df.head(10),
        x="channel",
        y="avg_views",
        color="avg_views",
        color_continuous_scale="purples",
        title="Top Channels by Avg views per video",
    )
    st.plotly_chart(fig5, use_container_width=True)

st.header("Best time to post")
fig6 = px.bar(
    time_df,
    x="hour",
    y="avg_views",
    color="avg_views",
    color_continuous_scale="oranges",
    title="Avg views by upload hour (UTC)",
)
st.plotly_chart(fig6, use_container_width=True)

st.header("Raw Data")
st.dataframe(keywords_df)
