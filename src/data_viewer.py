import streamlit as st
import json

# Load the JSON file
def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Assuming your JSON file is named "data.json" and is in the same directory as your Streamlit app
json_data = load_json("data/right_points.json")

# Display the JSON data
st.json(json_data)
