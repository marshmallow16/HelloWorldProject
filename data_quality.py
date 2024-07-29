import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'id': [1, 2, 2, 4, None],
    'value': [100, 200, 200, 400, None],
    'date': ['2021-01-01', '2021/02/01', '2021-03-01', '01-04-2021', '2021-05-01']
}
df = pd.DataFrame(data)

# Data Profiling
print(df.describe())
print(df.info())

# Data Cleansing
# Handle missing values
df['id'].fillna(df['id'].mean(), inplace=True)
df['value'].fillna(df['value'].mean(), inplace=True)

# Standardize date format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Data Deduplication
df.drop_duplicates(inplace=True)

# Data Validation
#assert df['id'].is_unique, "ID column contains duplicates"
#assert df['value'].notnull().all(), "Value column contains null values"

# Transformation Logic (Example: Scaling values)
df['value_scaled'] = df['value'] / df['value'].max()

# Monitoring (Example: Data Quality Metrics)
completeness = df.notnull().mean()
print("Completeness:\n", completeness)

# Logging (Simple example)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("ETL process completed successfully")
