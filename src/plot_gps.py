import pandas as pd
import streamlit as st

st.header("Plot of GPS data")

df = pd.read_json("data/right_points.json")
df.rename(columns={'lng': 'lon'}, inplace=True)

st.map(df, size=0.001)