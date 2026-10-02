import sqlite3
import pandas as pd

df = pd.read_csv("sales_clean.csv")
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
print(pd.read_sql("SELECT * FROM sales", conn))
conn.close()