import pandas as pd
import psycopg2
# Replace with your Neon connection details
conn_str = 'postgresql://neondb_owner:npg_HzBd69QwRWlP@ep-tiny-star-a8cyvi9i-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'
# Connect to the database
conn = psycopg2.connect(conn_str)
# Query the table and load into Pandas
df = pd.read_sql_query("SELECT * FROM employees;", conn)
# Show the DataFrame
print(df.head())
conn.close()