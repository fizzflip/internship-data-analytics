import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Set page layout
st.set_page_config(page_title="Uber Analytics", layout="wide")

# Loading the dataset
df = pd.read_csv("misc/datasets/uber-ncr-rides.csv")

# Menu configuration
with st.sidebar:
    selected = option_menu(
        "Dashboard",
        ["Dataset", "Overview", "Ride Analytics"],
        icons=["table", "bar-chart", "graph-up"],
        menu_icon="car-front",
        default_index=0,
    )

if selected == "Dataset":
    st.title("Dataset Explorer")
    st.divider()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Rows", df.shape[0])
    c2.metric("Total Columns", df.shape[1])
    c3.metric("Total Missing Values", df.isna().sum().sum())
    st.divider()

    st.dataframe(df, use_container_width=True)

if selected == "Overview":
    st.header("Overview")
    st.write("Insights on the dataset at-a-glance")
    st.subheader("Business Unit Performance Matrix")
    bu_matrix = df.groupby("Vehicle Type").agg(
        total_bookings=("Booking ID", "count"),
        revenue_generated=("Booking Value", "sum"),
        avg_distance=("Ride Distance", "mean"),
        avg_ratings=("Customer Rating", "mean"),
    )
    st.dataframe(bu_matrix)

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Operational Efficiency")
        st.write("Average Turnaround Time (minutes)")
        eff_df = df.groupby("Vehicle Type")[["Avg VTAT", "Avg CTAT"]].mean()
        st.dataframe(eff_df)

    with c2:
        st.subheader("Payment Method")
        st.write("Share of PMs across the platform")
        completed_ride = df[df["Booking Status"] == "Completed"]
        pay_summary = (
            completed_ride["Payment Method"].value_counts(normalize=True) * 100
        )
        st.dataframe(pay_summary)

    total_rides = len(df)
    st.subheader("Cancellation Audit")
    status_count = df["Booking Status"].value_counts().to_frame(name="Count")
    status_count["Share %"] = status_count["Count"] / total_rides * 100
    st.dataframe(status_count)

if selected == "Ride Analytics":
    st.title("Ride Analytics")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Vehicle Type vs Total Rides")

        fig, ax = plt.subplots(figsize=(6, 4))
        vehicle = df["Vehicle Type"].value_counts()
        ax.bar(vehicle.index, vehicle.values)
        ax.set_xlabel("Vehicle Type")
        ax.set_ylabel("Total Rides")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.caption("Vehicles that receive maximum bookings")
        st.caption("Helps identify most preferred category with customers")

    st.divider()

    st.subheader("Daily Booking Trend")
    user_input = st.number_input("Days:")
    daily = df.groupby("Date").size().head(int(user_input))

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(daily.index, daily.values, marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Bookings")
    plt.xticks(rotation=90)
    st.pyplot(fig)

    st.caption("Booking Volume Trend")
    st.caption("Helps identify peak demand days")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Ride Distance vs. Booking Value")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(df["Ride Distance"], df["Booking Value"])
        ax.set_xlabel("Ride Distance")
        ax.set_ylabel("Booking Value")
        st.pyplot(fig)

        st.caption("Correlation b/w Distance Traveled and Fare")

    with c2:
        st.subheader("Booking Status Distribution")
        status = df["Booking Status"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.barh(status.index, status.values)
        ax.set_xlabel("Count")
        st.pyplot(fig)

        st.caption("Customer Ride Status")
