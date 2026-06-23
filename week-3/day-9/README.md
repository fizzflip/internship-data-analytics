## Summary

Day 9 of the Data Analytics internship focused on practical, end-to-end data processing using the `pandas` library. The tasks involved importing real-world datasets from CSV and Excel files, extensively exploring and manipulating the data, applying mathematical operations and custom logic, and finally exporting the transformed data back to a new file.

## Key Learnings

### Advanced Pandas Operations

* **Data I/O:** Learned to read external files into DataFrames using `pd.read_csv()` and `pd.read_excel()`, and export processed DataFrames using `to_csv()`.
* **Data Access & Slicing:** Practiced retrieving specific columns using dictionary-style bracket notation, and accessing individual rows utilizing both label-based indexing (`.loc`) and positional indexing (`.iloc`).
* **Aggregation & Statistics:** Applied built-in aggregate functions such as `.min()`, `.max()`, and `.mean()` to calculate statistical summaries across numerical columns.
* **Filtering & Sorting:** Implemented Boolean indexing to filter rows conditionally (e.g., finding the class topper) and utilized `.sort_values()` to organize data hierarchically.
* **Custom Transformations:** Discovered how to apply custom Python functions to entire DataFrame columns using the `.apply()` method, and how to analyze categorical distributions using `.value_counts()`.

## Practical Application

### Student Data Analysis Pipeline

* **Data Ingestion:** Imported raw student academic scores from a standard CSV file (`student-data.csv`) into a Pandas DataFrame.
* **Metrics Calculation:** Engineered new columns to compute the "Total" marks across subjects and the rounded "Percentage" for each student.
* **Performance Analysis:** Filtered the dataset to identify high-performing students (e.g., scores > 80), located the overall class topper, and calculated subject-wise average marks.
* **Grading System:** Wrote a custom Python function to assign a letter grade based on calculated percentages and applied it across the entire dataset to generate a new "Grade" column.
* **Data Export:** Saved the enriched, modified DataFrame containing the newly calculated totals, percentages, and grades into a new file (`student-data-modified.csv`).
