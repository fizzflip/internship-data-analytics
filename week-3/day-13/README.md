## Summary

Day 13 of the Data Analytics internship focused extensively on data cleaning and preprocessing techniques using the
`pandas` library. The primary objective was taking a raw, messy dataset and systematically transforming it into a clean,
reliable format ready for analysis. Tasks involved handling missing values, coercing invalid data types, fixing
outliers, and engineering new features.

## Key Learnings

### Advanced Data Cleaning Pipeline

* **Data Coercion & Formatting:** Practiced forcing messy string columns into numeric types using `pd.to_numeric()` with
  `errors="coerce"` to safely handle unparseable text.
* **Handling Outliers & Anomalies:** Learned to identify and correct logical outliers, such as converting negative
  prices to absolute values using `map(lambda)` functions, and capping invalid ratings (e.g., ratings > 5).
* **Missing Value Imputation:** Utilized `.fillna()` to intelligently replace missing data (`NaN`) with calculated
  statistical approximations like the column mean or median.
* **Type Conversion:** Standardized the DataFrame's schema by explicitly casting columns to appropriate data types using
  `.astype()` (e.g., forcing quantities to integers and prices to floats).
* **Dynamic Row Insertion:** Explored methods to dynamically append new records to an existing DataFrame using
  `df.loc[len(df)]` combined with user input.

## Practical Application

### E-commerce Orders Data Cleansing

* **Raw Data Ingestion & Audit:** Loaded an imperfect e-commerce dataset and used `.isnull().sum()` and `.info()` to
  identify missing fields and incorrect data types.
* **Systematic Transformation:** Executed a multi-step cleaning script (`data_cleaning.py`) that coerced prices to
  numeric, corrected negative quantities, and replaced zero-value prices with the dataset's mean price.
* **Feature Engineering:** Created a `total_amount` column by multiplying the cleaned Price and Quantity, and generated
  a boolean `high_value_order` flag for orders exceeding a specific threshold.
* **Data Export:** Saved the finalized, clean dataset into a new CSV file (`ecommerce-orders-cleaned.csv`) for future
  downstream analysis.
