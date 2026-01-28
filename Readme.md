# 🧹 Sales Data Cleaner (Python ETL Project)

## 📌 Project Overview
**Sales Data Cleaner** is a Python-based ETL (Extract, Transform, Load) script designed to clean messy sales data stored in CSV format.  
The script removes duplicate records, sanitizes price values, converts USD prices to INR, and exports structured data into a JSON file for reporting or further analysis.

---

## 🎯 Project Goal
- Clean raw and inconsistent sales CSV data  
- Remove duplicate entries  
- Convert prices from **USD to INR**  
- Generate structured **JSON output**


---

## 🧠 Logic & Implementation

### 🔹 Approach
- Used list-based iteration to process CSV rows
- Maintained a checklist of `(product_name, price)` tuples
- Ensured only unique records were added
- Converted cleaned data into JSON format

### 🔹 Bug Encountered
- `float()` conversion failed due to:
- Dollar signs (`$`)
- Quotation marks (`"`)

### 🔹 Bug Fix
- Sanitized price strings using chained `.replace()` methods before conversion

Example:
```python
price = price.replace("$", "").replace('"', "")


## ⚙️ Setup Instructions

1. Save your raw sales data file as:
data.csv


2. Run the script:


python main.py


3. View the cleaned output in:


clean_sales.json


---


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