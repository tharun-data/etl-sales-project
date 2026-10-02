# ETL Sales Project

A simple Python ETL pipeline: CSV to SQLite using pandas.

## Steps
1. Extract: read `sales_raw.csv`
2. Transform (`transform.py`):
   - remove duplicate orders
   - standardize date format to YYYY-MM-DD
   - fix product name case
   - drop rows with missing quantity or price
   - add `total = quantity * price`
3. Load (`load.py`): save clean data into SQLite (`sales.db`)

## Run
pip install pandas
py transform.py
py load.py
