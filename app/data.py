import streamlit as st
import pandas as pd
import requests
from io import StringIO


# Load your data
@st.cache_data
def load_data():
    google_id = ""
    url = f"https://docs.google.com/spreadsheets/d/1qvDe5a66Vju5Cgp8v6Tty6MOhTdLQ0c6SzusIryDDi8/export?format=tsv&id=1qvDe5a66Vju5Cgp8v6Tty6MOhTdLQ0c6SzusIryDDi8&gid={google_id}"
    response = requests.get(url)
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data, sep="\t")
    return df


def show_data():
    data = load_data()
    st.title("All Practicums")

    st.sidebar.header("Filter Options")

    columns = data.columns.tolist()
    filtered_column = st.sidebar.selectbox("Select Column to Filter", columns)

    search_term = st.sidebar.text_input(f"Search for a value in {filtered_column}", "")

    selected_columns = st.sidebar.multiselect(
        "Select Columns to Display", options=columns, default=columns
    )

    filtered_data = data[selected_columns]

    if search_term:
        filtered_data = filtered_data[
            filtered_data[filtered_column]
            .astype(str)
            .str.contains(search_term, case=False, na=False)
        ]
    else:
        filtered_data = filtered_data

    st.write(f"Filtered Data for column: {filtered_column}")
    st.dataframe(filtered_data, width=1200, height=800)
