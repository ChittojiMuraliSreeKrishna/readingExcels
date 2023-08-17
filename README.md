# readingExcels
## libraries used XlsxWriter, pandas, psycopg2

### Pandas 
 used to create dataframes
### psycopg2
 used to read the csv files
### XlsxWriter
 used to create xlsx files

```bash
pip install pandas XlsxWriter psycopg2
```

to read the data from both csv and database

```python
# Merge DataFrames and identify different IDs
merged_data = pd.merge(csv_data, db_data, how='outer', on='id', indicator=True)
different_ids = merged_data[merged_data['_merge'] == 'left_only']
unique_ids = different_ids['id'].unique()
# Print different IDs
print("unique Values :", unique_ids)
```
we can edit the data from any side like from both database and csv by giving
```python
merged_data[merged_data['_merge'] == 'both']
```
or from left side i.e is from csv
```python
merged_data[merged_data['_merge'] == 'left_only']
```
or from right side i.e from database
```python
merged_data[merged_data['_merge'] == 'right_only']
```
