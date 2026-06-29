import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set custom colors for plots to make them modern and vibrant
plt.style.use("dark_background")
COLORS = ["#00d2ff", "#3a7bd5", "#a020f0", "#ff4b4b", "#f9a826", "#32cd32"]

POLLUTANTS = ["PM2_5", "PM10", "NO2", "CO_Level"]
CLEAN_POLLUTANT_NAMES = ["PM2.5", "PM10", "NO2", "CO"]


def style_axes(ax):
    """Helper function to remove borders from matplotlib charts for a cleaner look"""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(color="#333333", linestyle="--", linewidth=0.5, alpha=0.5)


def plot_top_cities(filtered_df, selected_country):
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
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    return fig


def plot_pollution_sources(filtered_df):
    source_counts = filtered_df["Pollution_Source"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(source_counts.index, source_counts.values, color=COLORS[4], edgecolor="none")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    style_axes(ax)
    fig.tight_layout()
    return fig


def plot_pollutant_averages(filtered_df):
    avg_pollutants = filtered_df[POLLUTANTS].mean()
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.bar(
        CLEAN_POLLUTANT_NAMES,
        avg_pollutants.values,
        color=COLORS[1],
        width=0.5,
        edgecolor="none",
    )
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
    fig.tight_layout()
    return fig


def plot_pollutant_trends(filtered_df):
    trend_df = filtered_df.groupby("Year")[POLLUTANTS].mean()
    fig, ax = plt.subplots(figsize=(10, 5))
    for i, pol in enumerate(POLLUTANTS):
        ax.plot(
            trend_df.index,
            trend_df[pol],
            marker="o",
            label=CLEAN_POLLUTANT_NAMES[i],
            linewidth=2,
            color=["#ff4b4b", "#00d2ff", "#f9a826", "#a020f0"][i],
        )
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Level")
    ax.set_xticks(trend_df.index)
    ax.legend(frameon=False, loc="upper right")
    style_axes(ax)
    fig.tight_layout()
    return fig


def plot_status_breakdown(filtered_df):
    status_counts = filtered_df["Air_Quality_Status"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    status_colors_map = {
        "Good": "#32cd32",
        "Moderate": "#f9a826",
        "Poor": "#ff7f50",
        "Very Poor": "#ff4b4b",
        "Hazardous": "#a020f0",
    }
    donut_colors = [
        status_colors_map.get(status, COLORS[i % len(COLORS)])
        for i, status in enumerate(status_counts.index)
    ]
    wedges, texts, autotexts = ax.pie(
        status_counts.values,
        labels=status_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=donut_colors,
        textprops=dict(color="w"),
    )
    centre_circle = plt.Circle((0, 0), 0.70, fc="#1e1e1e")
    fig.gca().add_artist(centre_circle)
    ax.axis("equal")
    fig.tight_layout()
    return fig


def plot_source_composition(filtered_df):
    source_pollutants = filtered_df.groupby("Pollution_Source")[POLLUTANTS].mean()

    # Sort pollutants by global mean (highest to lowest) so the largest is at the bottom
    global_means = filtered_df[POLLUTANTS].mean().sort_values(ascending=False)
    sorted_pollutants = global_means.index.tolist()

    fig, ax = plt.subplots(figsize=(8, 6))
    bottom = np.zeros(len(source_pollutants))
    for col in sorted_pollutants:
        i = POLLUTANTS.index(col)
        ax.bar(
            source_pollutants.index,
            source_pollutants[col],
            bottom=bottom,
            label=CLEAN_POLLUTANT_NAMES[i],
            color=COLORS[i % len(COLORS)],
            edgecolor="none",
        )
        bottom += source_pollutants[col].values
    ax.set_ylabel("Average Concentration")
    plt.xticks(rotation=45, ha="right")
    ax.legend(frameon=False, bbox_to_anchor=(1.05, 1), loc="upper left")
    style_axes(ax)
    fig.tight_layout()
    return fig


def plot_correlation_heatmap(filtered_df):
    corr_cols = ["AQI_Level"] + POLLUTANTS
    corr_matrix = filtered_df[corr_cols].corr()
    clean_corr_names = ["AQI"] + CLEAN_POLLUTANT_NAMES
    corr_matrix.index = clean_corr_names
    corr_matrix.columns = clean_corr_names
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        cbar_kws={"shrink": 0.8},
        ax=ax,
        linecolor="#1e1e1e",
    )
    ax.tick_params(colors="white")
    fig.tight_layout()
    return fig


def plot_aqi_variance(filtered_df, selected_country):
    if selected_country == "Global":
        top_groups = filtered_df["Country"].value_counts().nlargest(10).index
        box_df = filtered_df[filtered_df["Country"].isin(top_groups)]
        x_col = "Country"
    else:
        top_groups = filtered_df["City"].value_counts().nlargest(10).index
        box_df = filtered_df[filtered_df["City"].isin(top_groups)]
        x_col = "City"

    unique_groups = box_df[x_col].nunique()
    custom_palette = [COLORS[i % len(COLORS)] for i in range(unique_groups)]

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(
        data=box_df,
        x=x_col,
        y="AQI_Level",
        hue=x_col,
        palette=custom_palette,
        legend=False,
        ax=ax,
        flierprops={"marker": "x", "markeredgecolor": "#ff4b4b"},
    )
    ax.set_ylabel("AQI Level")
    ax.set_xlabel("")
    plt.xticks(rotation=45, ha="right")
    style_axes(ax)
    fig.tight_layout()
    return fig


def plot_aqi_distribution(filtered_df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(
        data=filtered_df,
        x="AQI_Level",
        kde=True,
        color=COLORS[0],
        edgecolor="none",
        ax=ax,
    )
    ax.set_xlabel("AQI Level")
    ax.set_ylabel("Frequency")
    style_axes(ax)
    fig.tight_layout()
    return fig


def plot_particle_clusters(filtered_df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=filtered_df,
        x="PM2_5",
        y="PM10",
        hue="Pollution_Source",
        palette="husl",
        s=60,
        alpha=0.7,
        ax=ax,
        edgecolor="none",
    )
    ax.set_xlabel("PM2.5 Level")
    ax.set_ylabel("PM10 Level")
    ax.legend(frameon=False, loc="best")
    style_axes(ax)
    fig.tight_layout()
    return fig
