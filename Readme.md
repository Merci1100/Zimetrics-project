# Sales Data Cleaner
1. Project Title & Goal
A Python ETL script that cleans messy sales CSV data, removes duplicates, and converts USD prices to INR for structured JSON reporting.

2. Setup Instructions
Save your raw data as data.csv.

Run the script: python main.py

View the result in clean_sales.json.

3. The Logic
Approach: I used a list-based iteration with a check list to track (name, price) tuples. This ensures only unique entries are added to the final JSON.

The Bug: The float() conversion crashed due to $ and " characters. I fixed this by using chained .replace() methods to sanitize the strings before processing.

4. Output Screenshots
5. Future Improvements
Validation: Use try-except blocks to handle missing data or corrupted rows.

Scalability: Implement with open() context managers to ensure better memory management for larger files.