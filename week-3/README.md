# Week 3: Advanced Pandas, APIs, and Streamlit Dashboards

## Summary

The third week of the Data Analytics internship focused on robust data processing, advanced API interactions, and building interactive web dashboards. The week started by diving deep into the `pandas` library for complex data manipulation and systematic data cleaning. We then explored dynamic API querying using the `requests` library. Finally, the week culminated in mastering the `streamlit` framework to combine data manipulation and visualization into full-fledged, interactive web applications.

## Daily Breakdown

### Day 9: Advanced Pandas Operations

- Focused on practical, end-to-end data processing pipelines using Pandas.
- **Practical:** Imported real-world datasets from CSV/Excel, calculated new metrics, applied custom grading functions using `.apply()`, filtered for high performers, and exported the cleaned data back to CSV.

### Day 10: Introduction to Streamlit

- Introduced web application development for data analytics using the `streamlit` library.
- **Practical:** Constructed a widget demonstration app, developed a secure multi-input user registration form using `st.form`, and built a multi-page dashboard shell using `streamlit_option_menu` and a sidebar.

### Day 11: Pandas and Streamlit Integration

- Bridged data manipulation with web visualization, focusing on data grouping and missing value handling.
- **Practical:** Managed `NaN` values using `.dropna()` and `.fillna()`. Executed complex multi-aggregations with `.groupby().agg()` and rendered the resulting business matrices directly into a Streamlit interface.

### Day 12: Advanced Web APIs

- Focused on dynamic interactions with web APIs and handling JSON responses.
- **Practical:** Built dynamic queries using request parameters (`params`) and custom headers. Handled connection errors and utilized `pd.json_normalize()` to flatten deeply nested API responses from TVMaze into Pandas DataFrames.

### Day 13: Systematic Data Cleaning

- Centered on taking a raw, messy e-commerce dataset and transforming it into a reliable format.
- **Practical:** Coerced invalid strings to numerics (`pd.to_numeric`), handled logical outliers using lambda functions, imputed missing data with statistical approximations (`.fillna`), and engineered new feature columns.

### Day 14: Full-Fledged Data Dashboard

- Culminated the week's learnings by developing a comprehensive "Uber Analytics" dashboard.
- **Practical:** Utilized advanced layout techniques (`st.columns`, `st.metric`) and embedded raw `matplotlib` figures (`st.pyplot`). Created an interactive app featuring a dataset explorer, detailed business overview matrices, and a dedicated ride analytics visualization tab.

## Skills Acquired

- **Advanced Pandas:** Mastery of `.apply()`, boolean filtering, grouping (`groupby`), multi-aggregation (`agg`), handling missing data, and type coercion.
- **Web Interfaces (Streamlit):** Building interactive dashboards with various input widgets, forms, sidebars, multi-page routing, column layouts, and KPI metrics.
- **Dynamic API Querying:** Constructing parameterized requests, utilizing HTTP headers, managing exceptions, and flattening complex JSON.
- **End-to-End Data Pipelines:** Managing the complete workflow from raw data ingestion and systematic cleaning to insightful visualization inside a web application.
