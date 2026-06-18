## Summary

Day 3 of my Data Analytics internship centered on mastering Python lists and building interactive command-line
applications. The tasks involved creating dynamic, menu-driven programs and expanding my proficiency in processing
external data by parsing JSON arrays from public APIs (ISRO spacecrafts and Mutual Funds).

## Key Learnings

### Python Lists and CLI Programs

* **List Manipulation:** Practiced appending elements, removing by value, and popping items by index.
* **Continuous Execution:** Utilized `while True` loops with `break` and `continue` to build persistent menu interfaces.
* **Sorting with Lambdas:** Advanced list usage by storing tuples (e.g., priority and task) and employing the `sorted()`
  function with a custom `lambda` key to automatically organize items.

### Data Processing and APIs

* **JSON Arrays:** Adapted to APIs returning top-level arrays instead of dictionaries, utilizing `len()` to gauge
  dataset sizes.
* **Linear Search:** Developed search algorithms to scan API responses and retrieve records matching user-provided IDs
  or scheme codes.

## Practical Application

### Interactive Scrapers and Task Management

* **Priority Task Manager:** Built a To-Do List application. Users can add prioritized tasks, view the sorted list, and
  delete entries via index operations.
* **ISRO Spacecraft Tracker:** Fetched data from the ISRO API to count total spacecraft and deployed a search feature to
  find specific crafts by ID.
* **Mutual Fund Search Tool:** Connected to a Mutual Fund API to extract scheme details, implementing a query system
  that returns scheme names based on numeric codes.
