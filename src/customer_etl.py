import pandas as pd

# 1. Read raw customer data
df = pd.read_csv("data/raw/customers.csv")

# 2. Display the data
print("Customer data:")
print(df)

# 3. Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Remove duplicate customers
df = df.drop_duplicates(subset=["customer_id"])

# 5. Identify invalid records
invalid_records = df[
    df["customer_name"].isnull() |
    df["city"].isnull()
]

# 6. Keep only valid records
valid_records = df[
    df["customer_name"].notnull() &
    df["city"].notnull()
]

# 7. Write valid records
valid_records.to_csv(
    "data/processed/customers_processed.csv",
    index=False
)

# 8. Write invalid records
invalid_records.to_csv(
    "data/processed/customer_rejects.csv",
    index=False
)

print("\nValid records:", len(valid_records))
print("Rejected records:", len(invalid_records))
print("\nCustomer ETL completed successfully!")