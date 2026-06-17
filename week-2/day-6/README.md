## Summary

Day 6 of the Data Analytics internship transitioned entirely into data visualization using the `matplotlib.pyplot` library. The primary focus was on learning how to visually represent datasets through various advanced charting techniques beyond standard line and bar graphs. Tasks involved visualizing stock trends, behavioral correlations, and sales distributions.

## Key Learnings

### Data Visualization with Matplotlib

* **Advanced Chart Types:** Explored specific plotting functions including `plt.fill_between()` for area graphs, `plt.scatter()` for scatter plots, `plt.stackplot()` for stacked area charts, and `plt.stem()` for stem charts.
* **Plot Customization:** Practiced enhancing chart readability by adding essential elements such as x and y-axis labels (`plt.xlabel`, `plt.ylabel`), descriptive titles (`plt.title`), and grid lines (`plt.grid`).
* **Visual Distinction:** Utilized colors, transparency (`alpha` channel), and legends (`plt.legend`) to differentiate between multiple datasets plotted on the same graph (e.g., distinguishing weekday vs. weekend data, or different product categories).

## Practical Application

### Matplotlib Plotting Exercises

* **Stock Trend Area Graph:** Created an overlapping area graph to compare the price trends of two different stocks over a sequence of days, utilizing the alpha parameter to ensure overlapping regions remained visible.
* **Behavioral Scatter Plot:** Developed a multi-scatter plot to visualize the correlation between sleep hours and phone usage, separating the data points into weekday and weekend categories using distinct colors and a legend.
* **Sales Stacked Plot:** Built a stacked area plot to represent the cumulative sales amounts of different electronics (AC, TV, Fridge) across bi-monthly periods.
* **Time-Series Stem Chart:** Implemented a stem chart to accurately visualize the discrete number of orders received at specific hourly intervals.
