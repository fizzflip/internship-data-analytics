import pandas as pd
import streamlit as st


@st.cache_data
def load_data(file_path: str) -> pd.DataFrame:
    """Loads the dataset, coordinates, and merges them to improve dashboard performance."""
    try:
        df = pd.read_csv(file_path)

        # Try to load and merge coordinates if they exist
        import os

        coords_path = "datasets/city_coordinates.csv"
        if os.path.exists(coords_path):
            coords_df = pd.read_csv(coords_path)
            df = df.merge(coords_df, on=["City", "Country"], how="left")

        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()


def get_filtered_data(
    df: pd.DataFrame, selected_country: str, selected_year: str
) -> pd.DataFrame:
    """Filters the dataframe based on selected country and year."""
    filtered_df = df.copy()

    if selected_country != "Global":
        filtered_df = filtered_df[filtered_df["Country"] == selected_country]

    if selected_year != "All Years":
        filtered_df = filtered_df[filtered_df["Year"] == int(selected_year)]

    return filtered_df


def get_kpis(df: pd.DataFrame):
    """Calculates KPIs from the dataframe."""
    if df.empty:
        return None, None, None

    avg_aqi = df["AQI_Level"].mean()

    # Safely find the worst city if the column exists and df is not empty
    worst_city_idx = df["AQI_Level"].idxmax()
    worst_city = (
        df.loc[worst_city_idx, "City"] if not pd.isna(worst_city_idx) else "N/A"
    )

    most_common_source = (
        df["Pollution_Source"].mode()[0] if not df["Pollution_Source"].empty else "N/A"
    )

    return avg_aqi, worst_city, most_common_source
