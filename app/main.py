import streamlit as st
from streamlit_navigation_bar import st_navbar

from data import show_data
from table import show_table

page = st_navbar(["All Practicums", "Individual Practicums"])

if page == "All Practicums":
    show_data()
elif page == "Individual Practicums":
    show_table()
