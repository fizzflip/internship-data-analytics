import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

df = pd.read_csv("misc/datasets/uber-ncr-rides.csv")

with st.sidebar:
    selected = option_menu(
        "Uber",
        options=["Dataset", "Overview", "Ride Analysis"],
        icons=["table", "bar-chart", "graph-up"],
        menu_icon="car-front",
        default_index=0,
    )

if selected == "Dataset":
    st.title("Dataset Explorer")
    st.divider()
    st.dataframe(df, use_container_width=True)


if selected == "Overview":
    st.title("Overview")
    st.subheader("Business Unit Performance Matrix")
    bu_matrix = df.groupby("Vehicle Type").agg(
        Total_bookings=("Booking ID", "count"),
        Revenue_generated=("Booking Value", "sum"),
        avg_distance=("Ride Distance", "mean"),
        avg_ratings=("Customer Rating", "mean"),
    )
    st.dataframe(bu_matrix)
