import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from process_data import load_data, get_filtered_data, get_kpis

# --- Page Config & Styling ---
st.set_page_config(
    page_title="AirLens Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply a sleek dark style to Matplotlib to blend with Streamlit's dark mode
plt.style.use("dark_background")

# Set custom colors for plots to make them modern and vibrant
COLORS = ["#00d2ff", "#3a7bd5", "#00d2ff", "#ff4b4b", "#f9a826"]

# --- Data Loading ---
DATASET_PATH = "air_quality_dataset.csv"  # Running from the project directory
df = load_data(DATASET_PATH)

if df.empty:
    st.stop()

# --- Sidebar Navigation ---
st.sidebar.title("🌍 AirLens Navigation")
page = st.sidebar.radio("Select Mode", ["Global Map View", "Analytics Dashboard"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Filters")
st.sidebar.markdown("Filter the data for specific regions or years.")

# Country Filter
countries = ["Global"] + sorted(df['Country'].unique().tolist())
selected_country = st.sidebar.selectbox("Select Region", countries, index=0)

# Year Filter
years = ["All Years"] + sorted(df['Year'].unique().tolist())
selected_year = st.sidebar.selectbox("Select Year", years, index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.markdown("AirLens is an AQI monitoring and analytics dashboard powered by Streamlit, Pandas, Matplotlib, and Plotly.")

# --- Filter Data ---
filtered_df = get_filtered_data(df, selected_country, selected_year)

# --- KPIs ---
avg_aqi, worst_city, most_common_source = get_kpis(filtered_df)

if page == "Global Map View":
    # --- Global Map View Page ---
    st.title("AirLens: Global AQI Heatmap")
    st.markdown("A geographic overview of Air Quality Indices around the world.")
    
    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Global Average AQI", value=f"{avg_aqi:.1f}" if avg_aqi else "N/A")
    with col2:
        st.metric(label="Most Polluted City", value=worst_city)
    with col3:
        st.metric(label="Dominant Pollution Source", value=most_common_source)
        
    st.markdown("---")
    
    # Create City-level AQI aggregation for the heatmap
    if 'Latitude' in filtered_df.columns and 'Longitude' in filtered_df.columns:
        city_aqi = filtered_df.groupby(['City', 'Country', 'Latitude', 'Longitude'])['AQI_Level'].mean().reset_index()
        
        # Create Plotly Mapbox Density map (Heatmap)
        fig_map = px.density_mapbox(
            city_aqi,
            lat='Latitude',
            lon='Longitude',
            z='AQI_Level',
            radius=20,
            hover_name='City',
            hover_data={'Country': True, 'Latitude': False, 'Longitude': False, 'AQI_Level': ':.1f'},
            color_continuous_scale=px.colors.sequential.YlOrRd,
            title="Global City AQI Heatmap",
            mapbox_style="carto-darkmatter",
            zoom=1
        )
        
        # Update map layout for a sleek full-width presentation
        fig_map.update_layout(
            margin=dict(l=0, r=0, t=50, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_map, use_container_width=True)
    else:
        st.warning("Coordinates not yet loaded. Please wait for coordinates to be fetched.")

elif page == "Analytics Dashboard":
    # --- Analytics Dashboard Page ---
    st.title("AirLens: Detailed Analytics")
    st.markdown("Analyze specific pollutant trends and environmental conditions.")
    
    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Average AQI Level", value=f"{avg_aqi:.1f}" if avg_aqi else "N/A")
    with col2:
        st.metric(label="Most Polluted City", value=worst_city)
    with col3:
        st.metric(label="Dominant Pollution Source", value=most_common_source)

    st.markdown("---")

    # Helper function to remove borders from matplotlib charts for a cleaner look
    def style_axes(ax):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(color='#333333', linestyle='--', linewidth=0.5, alpha=0.5)

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Top 10 Cities by AQI")
        
        # Sort cities by AQI
        top_cities = filtered_df.groupby('City')['AQI_Level'].mean().sort_values(ascending=False).head(10)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.barh(top_cities.index[::-1], top_cities.values[::-1], color=COLORS[0], edgecolor="none")
        ax.set_xlabel("Average AQI")
        style_axes(ax)
        
        # Remove y-axis ticks for a cleaner look
        ax.tick_params(axis='y', length=0)
        
        st.pyplot(fig, transparent=True)

    with col_chart2:
        st.subheader("Distribution of Pollution Sources")
        
        source_counts = filtered_df['Pollution_Source'].value_counts()
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(source_counts.index, source_counts.values, color=COLORS[4], edgecolor="none")
        ax.set_ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        style_axes(ax)
        
        st.pyplot(fig, transparent=True)

    st.markdown("---")
    st.subheader("Pollutant Averages (PM2.5, PM10, NO2, CO)")

    # Calculate averages for pollutants
    pollutants = ['PM2_5', 'PM10', 'NO2', 'CO_Level']
    avg_pollutants = filtered_df[pollutants].mean()

    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.bar(avg_pollutants.index, avg_pollutants.values, color=COLORS[1], width=0.5, edgecolor="none")

    # Add data labels
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 1), ha='center', va='bottom', color="white")

    ax.set_ylabel("Average Level")
    style_axes(ax)
    st.pyplot(fig, transparent=True)

    # Trend over years (only makes sense if "All Years" is selected)
    if selected_year == "All Years":
        st.markdown("---")
        st.subheader("Pollutant Trends Over the Years")
        
        trend_df = filtered_df.groupby('Year')[pollutants].mean()
        
        fig, ax = plt.subplots(figsize=(10, 5))
        for i, pol in enumerate(pollutants):
            ax.plot(trend_df.index, trend_df[pol], marker='o', label=pol, linewidth=2, color=["#ff4b4b", "#00d2ff", "#f9a826", "#a020f0"][i])
        
        ax.set_xlabel("Year")
        ax.set_ylabel("Average Level")
        
        # Ensure x-axis ticks are integers
        ax.set_xticks(trend_df.index)
        
        ax.legend(frameon=False, loc="upper right")
        style_axes(ax)
        st.pyplot(fig, transparent=True)
