import streamlit as st
import plotly.express as px
import pandas as pd

# Load your dataset
df = pd.read_csv("world_happiness.csv")  # adjust to your file path

st.title("🌍 World Happiness Interactive Bubble Plot")

# Filter to a single year for visualization
df_2024 = df[df["Year"] == 2024]

# Create bubble plot
fig = px.scatter(
    df_2024,
    x="GDP per capita",
    y="Life evaluation",
    size="Social support",
    color="Freedom",
    hover_name="Country",
    size_max=60,
    title="GDP vs Life Evaluation (2024)"
)

st.plotly_chart(fig, use_container_width=True)
