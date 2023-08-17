import pandas as pd
import psycopg2

# Load CSV data into pandas DataFrame
csv_data = pd.read_csv('./exam_data.csv')
print(csv_data.head)
try:    
# Connect to PostgreSQL
    conn = psycopg2.connect(
    dbname='database1',
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
    )
    print("successfiully connected")
except Exception as e:
    print(e)

# Query PostgreSQL data
query = "SELECT * FROM test_table"
db_data = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Merge DataFrames and identify different IDs
merged_data = pd.merge(csv_data, db_data, how='outer', on='id', indicator=True)
different_ids = merged_data[merged_data['_merge'] == 'left_only']
unique_ids = different_ids['id'].unique()
# Print different IDs
print("unique Values :", unique_ids)

# Convert unique IDs to a DataFrame
unique_ids_df = pd.DataFrame({'unique_ids': unique_ids})

# Write the unique IDs to a new Excel file
excel_writer = pd.ExcelWriter('unique_ids.xlsx', engine='xlsxwriter')
unique_ids_df.to_excel(excel_writer, sheet_name='Sheet1', index=False)
excel_writer._save()

print("Unique IDs written to 'unique_ids.xlsx'")

