import streamlit as st
import pandas as pd
import json

st.title("CSV/Excel to JSON Converter (Array of Objects)")


uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

        # Replace NaN values with None
        df = df.where(pd.notnull(df), None)

        # Convert DataFrame to a list of dictionaries (objects)
        json_data = df.to_dict(orient="records")

        # Display a preview of the parsed data
        st.write("Preview of parsed data (First 5 objects):")
        st.dataframe(df.head())
        # st.json(json_data[:5])  # Show only the first 5 objects

        def convert_to_json_string(data):
            return json.dumps(data, indent=4)  # Add indentation for readability

        json_string = convert_to_json_string(json_data)

        st.download_button(
            label="Download JSON",
            data=json_string,
            file_name=f"{uploaded_file.name.split('.')[0]}.json",
            mime="application/json",
        )
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a CSV or Excel file to convert to JSON.")
