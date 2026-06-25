## Summary

Day 12 of the Data Analytics internship focused on advanced interactions with web APIs using the `requests` library. The primary objectives were learning how to construct dynamic queries using request parameters, handling common network exceptions gracefully, and instantly converting complex API JSON responses into structured Pandas DataFrames for immediate analysis.

## Key Learnings

### Advanced API Integration

* **Dynamic Query Parameters:** Transitioned from hardcoded URLs to using the `params` argument in `requests.get()`. This enables building dynamic API queries safely based on user input without manual string concatenation.
* **HTTP Headers:** Learned how to pass custom HTTP headers (e.g., `User-Agent`) in requests to bypass basic scraping blocks and successfully communicate with stricter servers.
* **Error Handling:** Implemented robust `try-except` blocks to catch network issues like `ConnectionError`, and utilized `response.raise_for_status()` to automatically flag bad HTTP responses (like 404 or 500 errors).
* **JSON Normalization:** Introduced `pd.json_normalize()` from the pandas library, an extremely powerful method for flattening deeply nested JSON API responses straight into clean, 2D DataFrames.

## Practical Application

### Dynamic API Scripts

* **Postal Pincode Fetcher:** Created a script that queries a pincode API, successfully integrating a custom User-Agent header and demonstrating comprehensive `try-except` error handling for resilient data fetching.
* **University Search Tool:** Built an interactive script that asks for a country name, passes it as a query parameter to a university database API, and returns the total count of universities found.
* **TV Show Database Query:** Developed a search tool utilizing the TVMaze API. It dynamically searches for user-inputted TV shows and immediately flattens the resulting complex JSON response into a tabular Pandas DataFrame using `json_normalize`.
