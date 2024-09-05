import streamlit as st
import pandas as pd
import requests
from io import StringIO


@st.cache_data
def load_data():
    google_id = ""
    url = f"https://docs.google.com/spreadsheets/d/1qvDe5a66Vju5Cgp8v6Tty6MOhTdLQ0c6SzusIryDDi8/export?format=tsv&id=1qvDe5a66Vju5Cgp8v6Tty6MOhTdLQ0c6SzusIryDDi8&gid={google_id}"
    response = requests.get(url)
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data, sep="\t")
    return df


def show_table():
    df = load_data()

    st.title("Individual Practicums")

    names = df["Company Name"].unique()
    selected_name = st.selectbox("Select a Name", names)

    filtered_row = df[df["Company Name"] == selected_name]

    if not filtered_row.empty:
        row = filtered_row.iloc[0]
        column_headings = df.columns
        markdown_table = "| Column | Value |\n"
        markdown_table += "| ------- | ----- |\n"
        for heading in column_headings:
            markdown_table += f"| {heading} | {row[heading]} |\n"
        st.markdown(f"### {row['Company Name']} \n{markdown_table}")
    else:
        st.write("No data found for the selected name.")
