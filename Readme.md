# 🧹 Problem 2: Sales Data Cleaner (Python ETL Project)

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

```
## ⚙️ Setup Instructions

1. Save your raw sales data file as:

Sales.csv


2. Run the script:


python main.py


3. View the cleaned output in:


clean_sales.json

## 📸 Output Screenshots

### Raw CSV Input
![Raw CSV Data](screenshots/data_csv.png)

### Cleaned JSON Output
![Clean JSON Output](screenshots/clean_sales_json.png)

---

## 🚀 Future Improvements

### ✅ Validation
- Implement `try-except` blocks to gracefully handle:
  - Missing or null values
  - Corrupted or malformed rows
  - Invalid numeric formats during conversion

### ✅ Scalability
- Use `with open()` context managers to:
  - Ensure safe file handling
  - Improve memory efficiency
  - Support large-scale CSV processing



