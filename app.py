import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Sber Neuro Metrics Lab")
st.title("Sber Neuro Metrics Lab")

# Sidebar
st.sidebar.header("Data Upload")

uploaded_data = st.sidebar.file_uploader("Upload Data File", type=["xlsx", "csv"])
uploaded_meta = st.sidebar.file_uploader("Upload Variable Description", type=["xlsx"])

process_button = st.sidebar.button("Process Data")

# Logic
if uploaded_data and uploaded_meta:
    try:
        # Load Data File
        if uploaded_data.name.endswith('.csv'):
            df_data = pd.read_csv(uploaded_data)
        else:
            df_data = pd.read_excel(uploaded_data)

        # Load Meta File
        df_meta = pd.read_excel(uploaded_meta)

        # Display Previews
        st.subheader("Data Preview")
        st.dataframe(df_data.head())

        st.subheader("Variable Description Preview")
        st.dataframe(df_meta.head())

        if process_button:
            st.info("Processing started...")
            # Placeholder for future processing logic

    except Exception as e:
        st.error(f"Error loading files: {e}")

elif uploaded_data or uploaded_meta:
    # One is missing
    st.warning("Please upload both files")

else:
    # None uploaded
    st.info("Please upload data and variable description files to begin.")
