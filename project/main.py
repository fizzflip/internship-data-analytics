import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
from process_data import get_filtered_data, get_kpis, load_data
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_option_menu import option_menu

# --- Page Config & Styling ---
st.set_page_config(
    page_title="AirLens Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply a sleek dark style to Matplotlib to blend with Streamlit's dark mode
plt.style.use("dark_background")

# Set custom colors for plots to make them modern and vibrant
COLORS = ["#00d2ff", "#3a7bd5", "#a020f0", "#ff4b4b", "#f9a826", "#32cd32"]

# --- Data Loading ---
DATASET_PATH = "air_quality_dataset.csv"  # Running from the project directory
df = load_data(DATASET_PATH)

if df.empty:
    st.stop()

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("🌍 AirLens Navigation")
    page = option_menu(
        menu_title=None,
        options=["Global Map View", "Analytics Dashboard"],
        icons=["globe-americas", "bar-chart-line"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00d2ff", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#333333",
            },
            "nav-link-selected": {"background-color": "#1e1e1e"},
        },
    )

st.sidebar.markdown("---")
st.sidebar.markdown("### Filters")
st.sidebar.markdown("Filter the data for specific regions or years.")

# Country Filter
countries = ["Global"] + sorted(df["Country"].unique().tolist())
selected_country = st.sidebar.selectbox("Select Region", countries, index=0)

# Year Filter
years = ["All Years"] + sorted(df["Year"].unique().tolist())
selected_year = st.sidebar.selectbox("Select Year", years, index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.markdown(
    "AirLens is an AQI monitoring and analytics dashboard powered by Streamlit, Pandas, Matplotlib, and Plotly."
)

# --- Filter Data ---
filtered_df = get_filtered_data(df, selected_country, selected_year)

# --- KPIs ---
avg_aqi, worst_city, most_common_source = get_kpis(filtered_df)

if page == "Global Map View":
    # --- Global Map View Page ---
    st.title(f"AirLens: {'Global' if selected_country == 'Global' else selected_country} AQI Heatmap")
    st.markdown(f"A geographic overview of Air Quality Indices {'around the world' if selected_country == 'Global' else 'in ' + selected_country}.")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label=f"{'Global ' if selected_country == 'Global' else ''}Average AQI", value=f"{avg_aqi:.1f}" if avg_aqi else "N/A"
        )
    with col2:
        st.metric(label="Most Polluted City", value=worst_city)
    with col3:
        st.metric(label="Dominant Pollution Source", value=most_common_source)

    style_metric_cards(
        background_color="#1e1e1e",
        border_size_px=1,
        border_color="#333333",
        border_radius_px=10,
        border_left_color="#00d2ff",
    )

    st.markdown("---")

    # Create City-level AQI aggregation for the heatmap
    if "Latitude" in filtered_df.columns and "Longitude" in filtered_df.columns:
        city_aqi = (
            filtered_df.groupby(["City", "Country", "Latitude", "Longitude"])[
                "AQI_Level"
            ]
            .mean()
            .reset_index()
        )

        # Create Plotly Density map (Heatmap)
        fig_map = px.density_map(
            city_aqi,
            lat="Latitude",
            lon="Longitude",
            z="AQI_Level",
            radius=20,
            hover_name="City",
            hover_data={
                "Country": True,
                "Latitude": False,
                "Longitude": False,
                "AQI_Level": ":.1f",
            },
            color_continuous_scale=px.colors.sequential.YlOrRd,
            title=f"{'Global' if selected_country == 'Global' else selected_country} City AQI Heatmap",
            map_style="carto-darkmatter",
            zoom=1,
        )

        # Update map layout for a sleek full-width presentation
        fig_map.update_layout(
            margin=dict(l=0, r=0, t=50, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        st.plotly_chart(fig_map, width="stretch")
    else:
        st.warning(
            "Coordinates not yet loaded. Please wait for coordinates to be fetched."
        )

elif page == "Analytics Dashboard":
    # --- Analytics Dashboard Page ---
    st.title(f"AirLens: {'Global' if selected_country == 'Global' else selected_country} Detailed Analytics")
    st.markdown("Analyze specific pollutant trends and environmental conditions.")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Average AQI Level", value=f"{avg_aqi:.1f}" if avg_aqi else "N/A"
        )
    with col2:
        st.metric(label="Most Polluted City", value=worst_city)
    with col3:
        st.metric(label="Dominant Pollution Source", value=most_common_source)

    style_metric_cards(
        background_color="#1e1e1e",
        border_size_px=1,
        border_color="#333333",
        border_radius_px=10,
        border_left_color="#00d2ff",
    )

    st.markdown("---")

    # Helper function to remove borders from matplotlib charts for a cleaner look
    def style_axes(ax):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(color="#333333", linestyle="--", linewidth=0.5, alpha=0.5)

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader(f"Top 10 Cities by AQI {'Globally' if selected_country == 'Global' else 'in ' + selected_country}")

        # Sort cities by AQI
        top_cities = (
            filtered_df.groupby("City")["AQI_Level"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.barh(
            top_cities.index[::-1],
            top_cities.values[::-1],
            color=COLORS[0],
            edgecolor="none",
        )
        ax.set_xlabel("Average AQI")
        style_axes(ax)

        # Remove y-axis ticks for a cleaner look
        ax.tick_params(axis="y", length=0)

        st.pyplot(fig, transparent=True)

    with col_chart2:
        st.subheader(f"Distribution of Pollution Sources {'Globally' if selected_country == 'Global' else 'in ' + selected_country}")

        source_counts = filtered_df["Pollution_Source"].value_counts()

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(
            source_counts.index, source_counts.values, color=COLORS[4], edgecolor="none"
        )
        ax.set_ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        style_axes(ax)

        st.pyplot(fig, transparent=True)

    st.markdown("---")
    st.subheader(f"Pollutant Averages {'Globally' if selected_country == 'Global' else 'in ' + selected_country} (PM2.5, PM10, NO2, CO)")

    # Calculate averages for pollutants
    pollutants = ["PM2_5", "PM10", "NO2", "CO_Level"]
    clean_pollutant_names = ["PM2.5", "PM10", "NO2", "CO"]
    avg_pollutants = filtered_df[pollutants].mean()

    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.bar(
        clean_pollutant_names,
        avg_pollutants.values,
        color=COLORS[1],
        width=0.5,
        edgecolor="none",
    )

    # Add data labels
    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 1,
            round(yval, 1),
            ha="center",
            va="bottom",
            color="white",
        )

    ax.set_ylabel("Average Level")
    style_axes(ax)
    st.pyplot(fig, transparent=True)

    # Trend over years (only makes sense if "All Years" is selected)
    if selected_year == "All Years":
        st.markdown("---")
        st.subheader("Pollutant Trends Over the Years")

        trend_df = filtered_df.groupby("Year")[pollutants].mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        for i, pol in enumerate(pollutants):
            ax.plot(
                trend_df.index,
                trend_df[pol],
                marker="o",
                label=clean_pollutant_names[i],
                linewidth=2,
                color=["#ff4b4b", "#00d2ff", "#f9a826", "#a020f0"][i],
            )

        ax.set_xlabel("Year")
        ax.set_ylabel("Average Level")

        # Ensure x-axis ticks are integers
        ax.set_xticks(trend_df.index)

        ax.legend(frameon=False, loc="upper right")
        style_axes(ax)
        st.pyplot(fig, transparent=True)

    st.markdown("---")
    st.subheader("Advanced Data Analysis")

    col_chart3, col_chart4 = st.columns(2)

    with col_chart3:
        st.markdown("**Air Quality Status Breakdown**")
        status_counts = filtered_df["Air_Quality_Status"].value_counts()
        
        fig, ax = plt.subplots(figsize=(6, 6))
        status_colors_map = {
            "Good": "#32cd32",        # Green
            "Moderate": "#f9a826",    # Yellow/Orange
            "Poor": "#ff7f50",        # Coral/Orange-Red
            "Very Poor": "#ff4b4b",   # Red
            "Hazardous": "#a020f0",   # Purple
        }
        
        # Default to a random color from COLORS if the status isn't in the map
        donut_colors = [status_colors_map.get(status, COLORS[i % len(COLORS)]) for i, status in enumerate(status_counts.index)]
        
        # Use a donut chart
        wedges, texts, autotexts = ax.pie(
            status_counts.values, 
            labels=status_counts.index, 
            autopct='%1.1f%%',
            startangle=90,
            colors=donut_colors,
            textprops=dict(color="w")
        )
        
        # Draw white circle in the middle
        centre_circle = plt.Circle((0,0),0.70,fc='#1e1e1e')
        fig.gca().add_artist(centre_circle)
        ax.axis('equal')  
        st.pyplot(fig, transparent=True)

    with col_chart4:
        st.markdown("**Pollutant Composition by Source**")
        # Stacked bar chart showing average pollutants for each source
        source_pollutants = filtered_df.groupby("Pollution_Source")[pollutants].mean()
        
        fig, ax = plt.subplots(figsize=(8, 6))
        
        bottom = np.zeros(len(source_pollutants))
        for i, col in enumerate(pollutants):
            ax.bar(
                source_pollutants.index, 
                source_pollutants[col], 
                bottom=bottom, 
                label=clean_pollutant_names[i],
                color=COLORS[i % len(COLORS)],
                edgecolor="none"
            )
            bottom += source_pollutants[col].values
            
        ax.set_ylabel("Average Concentration")
        plt.xticks(rotation=45, ha="right")
        ax.legend(frameon=False, bbox_to_anchor=(1.05, 1), loc='upper left')
        style_axes(ax)
        st.pyplot(fig, transparent=True)

    st.markdown("---")
    st.subheader("Pollutant Correlation Analysis")
    st.markdown("Discover which pollutants are driving the AQI levels the hardest.")

    # Correlation Heatmap
    corr_cols = ["AQI_Level"] + pollutants
    corr_matrix = filtered_df[corr_cols].corr()
    
    # Rename index and columns for cleaner display
    clean_corr_names = ["AQI"] + clean_pollutant_names
    corr_matrix.index = clean_corr_names
    corr_matrix.columns = clean_corr_names

    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Custom dark heatmap using seaborn
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        cmap="coolwarm", 
        fmt=".2f", 
        linewidths=.5, 
        cbar_kws={"shrink": .8},
        ax=ax,
        linecolor="#1e1e1e"
    )
    
    # Tweak text colors for dark mode readability
    ax.tick_params(colors='white')
    st.pyplot(fig, transparent=True)
    
    st.markdown("---")
    st.subheader("Deep Dive Analytics")
    st.markdown("Explore data distributions, regional variances, and particle-size clusters.")

    # 1. AQI Variance (Boxplot) - Full Width
    if selected_country == "Global":
        st.markdown("**AQI Variance Across Top Countries**")
        # Get top 10 countries by record count
        top_groups = filtered_df['Country'].value_counts().nlargest(10).index
        box_df = filtered_df[filtered_df['Country'].isin(top_groups)]
        x_col = 'Country'
    else:
        st.markdown(f"**AQI Variance Across Top Cities in {selected_country}**")
        # Get top 10 cities by record count in that country
        top_groups = filtered_df['City'].value_counts().nlargest(10).index
        box_df = filtered_df[filtered_df['City'].isin(top_groups)]
        x_col = 'City'
    
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(
        data=box_df, 
        x=x_col, 
        y='AQI_Level', 
        palette=COLORS,
        ax=ax,
        flierprops={"marker": "x", "markeredgecolor": "#ff4b4b"}
    )
    
    ax.set_ylabel("AQI Level")
    ax.set_xlabel("")
    plt.xticks(rotation=45, ha="right")
    style_axes(ax)
    st.pyplot(fig, transparent=True)
    
    col_chart5, col_chart6 = st.columns(2)
    
    with col_chart5:
        # 2. Global AQI Distribution Profile (Histogram + KDE)
        st.markdown(f"**{'Global' if selected_country == 'Global' else selected_country} AQI Distribution Profile**")
        fig, ax = plt.subplots(figsize=(8, 6))
        
        sns.histplot(
            data=filtered_df,
            x='AQI_Level',
            kde=True,
            color=COLORS[0],
            edgecolor="none",
            ax=ax
        )
        
        ax.set_xlabel("AQI Level")
        ax.set_ylabel("Frequency")
        style_axes(ax)
        st.pyplot(fig, transparent=True)

    with col_chart6:
        # 3. Particle Size Cluster Analysis (Scatter Plot)
        st.markdown("**Particle Size Cluster Analysis (PM2.5 vs PM10)**")
        fig, ax = plt.subplots(figsize=(8, 6))
        
        sns.scatterplot(
            data=filtered_df,
            x='PM2_5',
            y='PM10',
            hue='Pollution_Source',
            palette="husl",
            s=60,
            alpha=0.7,
            ax=ax,
            edgecolor="none"
        )
        
        ax.set_xlabel("PM2.5 Level")
        ax.set_ylabel("PM10 Level")
        ax.legend(frameon=False, bbox_to_anchor=(1.05, 1), loc='upper left')
        style_axes(ax)
        st.pyplot(fig, transparent=True)
