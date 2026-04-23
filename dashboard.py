import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("analysis.csv")

st.title("Youtube Niche Analyzer")
st.subheader("Top Keywords by Frequency")

fig1 = px.bar(
    df.head(15),
    x="keyword",
    y="frequency",
    color="frequency",
    color_continuous_scale="blues",
    title="Most Common Keywords in Titles",
)
st.plotly_chart(fig1)

st.subheader("Average Views per Keyword")

fig2 = px.bar(
    df.head(15),
    x="keyword",
    y="avg_views",
    color="avg_views",
    color_continuous_scale="reds",
    title="Which Keywords Get the Most Views?",
)
st.plotly_chart(fig2)

st.subheader("Frequency vs Avg Views")

fig3 = px.scatter(
    df,
    x="frequency",
    y="avg_views",
    text="keyword",
    title="Keyword Frequency vs Average Views",
    labels={"frequency": "How Often It Appears", "avg_views": "Avg View Count"},
)
fig3.update_traces(textposition="top center")
st.plotly_chart(fig3)

st.dataframe(df)
