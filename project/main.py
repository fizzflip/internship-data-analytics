import pandas as pd
import plotly.express as px
import streamlit as st
import visualizations as vis
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

# The color definitions and matplotlib styling have been moved to visualizations.py


def centered_caption(text):
    st.markdown(
        f"<p style='text-align: center; color: #888888; font-size: 0.85em; margin-top: -10px;'>{text}</p>",
        unsafe_allow_html=True,
    )


# --- Data Loading ---
DATASET_PATH = "datasets/air_quality_dataset.csv"  # Running from the project directory
df = load_data(DATASET_PATH)

if df.empty:
    st.stop()

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("Airlens")
    page = option_menu(
        menu_title=None,
        options=["Map View", "Analytics Dashboard"],
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

if page == "Map View":
    # --- Global Map View Page ---
    st.title(
        f"{'Global' if selected_country == 'Global' else selected_country} AQI Heatmap"
    )
    st.markdown(
        f"A geographic overview of Air Quality Indices {'around the world' if selected_country == 'Global' else 'in ' + selected_country}."
    )

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label=f"Average AQI", value=f"{avg_aqi:.1f}" if avg_aqi else "N/A")
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

    st.divider()

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
            title=f"{'Global' if selected_country == 'Global' else selected_country} AQI Heatmap",
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
    st.title(
        f"{'Global' if selected_country == 'Global' else selected_country} Detailed Analytics"
    )
    st.markdown("Analyze specific pollutant trends and environmental conditions.")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    # --- Tabbed Layout ---
    tab1, tab2, tab3 = st.tabs(["Overview", "Deep Dive", "Correlations & Trends"])

    with tab1:
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

        st.divider()
        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            fig1 = vis.plot_top_cities(filtered_df, selected_country)
            st.pyplot(fig1, transparent=True)
            centered_caption(
                f"Top 10 Cities by AQI {'Globally' if selected_country == 'Global' else 'in ' + selected_country}"
            )

        with col_chart2:
            fig2 = vis.plot_pollution_sources(filtered_df)
            st.pyplot(fig2, transparent=True)
            centered_caption(
                f"Distribution of Pollution Sources {'Globally' if selected_country == 'Global' else 'in ' + selected_country}"
            )

        st.divider()
        fig3 = vis.plot_pollutant_averages(filtered_df)
        st.pyplot(fig3, transparent=True)
        centered_caption(
            f"Pollutant Averages {'Globally' if selected_country == 'Global' else 'in ' + selected_country} (PM2.5, PM10, NO2, CO)"
        )

    with tab2:
        col_chart3, col_chart4 = st.columns(2)
        with col_chart3:
            fig6 = vis.plot_particle_clusters(filtered_df)
            st.pyplot(fig6, transparent=True)
            centered_caption("Particle Size Cluster Analysis (PM2.5 vs PM10)")

        with col_chart4:
            fig5 = vis.plot_aqi_distribution(filtered_df)
            st.pyplot(fig5, transparent=True)
            centered_caption(
                f"{'Global' if selected_country == 'Global' else selected_country} AQI Distribution Profile"
            )

        st.divider()
        fig4 = vis.plot_aqi_variance(filtered_df, selected_country)
        st.pyplot(fig4, transparent=True)
        if selected_country == "Global":
            centered_caption("AQI Variance Across Top Countries")
        else:
            centered_caption(f"AQI Variance Across Top Cities in {selected_country}")

        st.divider()
        fig7 = vis.plot_source_composition(filtered_df)
        st.pyplot(fig7, transparent=True)
        centered_caption("Pollutant Composition by Source")

    with tab3:
        # Trend over years (only makes sense if "All Years" is selected)
        if selected_year == "All Years":
            fig10 = vis.plot_pollutant_trends(filtered_df)
            st.pyplot(fig10, transparent=True)
            centered_caption("Pollutant Trends Over the Years")
            st.divider()

        col_chart5, col_chart6 = st.columns(2)

        with col_chart5:
            fig8 = vis.plot_status_breakdown(filtered_df)
            st.pyplot(fig8, transparent=True)
            centered_caption("Air Quality Status Breakdown")

        with col_chart6:
            fig9 = vis.plot_correlation_heatmap(filtered_df)
            st.pyplot(fig9, transparent=True)
            centered_caption("Pollutant Correlation Analysis")
