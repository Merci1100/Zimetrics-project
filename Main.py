""""Problem 2: The "Sales Data" Cleaner
• Theme: Data Engineering (ETL)
• Goal: Write a script to process a messy CSV file and generate a clean JSON report.
• Input (Create a file sales.csv with this data):

1 101, "Widget A", $10.50, USA
2 102, Widget B, $5.00, Canada
3 103, Widget A, 10.50, USA

CSV

• Requirements:
1. Read the CSV file.
2. Clean: Remove $ signs and quotes. Convert prices to Float.
3. Deduplicate: Remove duplicate rows (same Product & Price).
4. Convert: Convert all USD prices to INR (Assume 1 USD = 83 INR).
5. Output: Save the clean data to clean_sales.json .
• The "Ask" (Screenshot Proof):
• Screenshot of the final clean_sales.json file opened in a text editor showing the clean data."""
import csv
import json

def json_conversion(filename):
# 1. EXTRACT: Open the source CSV file and convert it into a list for processing
    f=open(filename, 'r')
    reader=list(csv.reader(f))

    print(list(reader))
    
    jsonfile=[]

    check=[]
# 2. TRANSFORM: Loop through each row of the CSV data
    for i in range(len(reader)):
        id= int(reader[i][0].strip())
        name=reader[i][1].replace('"',"").replace("'","").strip()
        price= float(reader[i][2].replace("$","")) *83
        cont=reader[i][3].strip()
# 3. DEDUPLICATION: Only add the item if the (name, price) combo hasn't been seen    
        if (name,  price) in check:
            continue
        else :
            check.append((name,price))
            jsonfile.append(
                { "id":id,
                "name":name,
                "price":price,
                "country" :cont            
                }
            )

    print(jsonfile)
# 4. LOAD: Export the cleaned list into a JSON file with tab indentation
    json.dump(jsonfile,open("clean_sales.json","w"),indent="\t")
# Execute the function
json_conversion("sales.csv")


    