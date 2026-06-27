## Summary

Day 11 of the Data Analytics internship bridged data manipulation with web visualization by integrating `pandas` and `streamlit`. The day's tasks focused on essential data preprocessing steps—such as handling missing values and performing complex grouping operations—and then dynamically displaying those processed data structures directly within a Streamlit web application.

## Key Learnings

### Advanced Pandas Operations

- **Missing Data Handling:** Explored techniques to manage missing data (`NaN` values from `numpy`), specifically using `.dropna()` to remove incomplete records and `.fillna()` to impute missing spots with default values (like -1).
- **Data Grouping (`groupby`):** Learned how to categorize datasets based on categorical columns (e.g., grouping by department).
- **Multi-Aggregation (`agg`):** Practiced applying multiple statistical functions simultaneously (`sum`, `mean`, `max`) to grouped data. Further advanced this by creating custom-named aggregated columns (e.g., `Total_bookings=("Booking ID", "count")`).

### Streamlit Data Integration

- **Data Rendering:** Utilized `st.dataframe()` to elegantly render Pandas DataFrames natively inside the Streamlit web interface.
- **Streamlit Components:** Integrated the `streamlit_option_menu` for side-bar navigation, building a multi-view application that logically separates the raw dataset view from the analytical overview.

## Practical Application

### Analytical Dashboard & Scripts

- **Null Value Script:** Wrote a fundamental script to simulate and resolve missing student marks, establishing the baseline for data cleaning.
- **Salary Aggregation Script:** Created a department-wise salary analysis script to practice the syntax of `groupby` and simultaneous multi-aggregation.
- **Uber Ride Analysis Dashboard:** Developed an interactive web dashboard that loads real-world Uber NCR ride data. It features a navigation sidebar that allows users to toggle between viewing the raw dataset and an "Overview" page. The overview page calculates and displays a Business Unit Performance Matrix, showcasing total bookings, revenue, and averages grouped dynamically by vehicle type.
