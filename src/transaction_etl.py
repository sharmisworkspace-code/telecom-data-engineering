import pandas as pd

# 1. Read raw transaction data
df = pd.read_csv("data/raw/transactions.csv")

# 2. Display the transaction data
print("Transaction data:")
print(df)

# 3. Check for missing values
print("\nMissing values:")
print(df.isnull().sum())
# 4. Check for invalid transaction amounts
invalid_amounts = df[df["amount"] <= 0]

print("\nInvalid transaction amounts:")
print(invalid_amounts)
# 5. Check for invalid transaction status
valid_statuses = ["SUCCESS", "FAILED"]

invalid_status = df[~df["status"].isin(valid_statuses)]

print("\nInvalid transaction statuses:")
print(invalid_status)
# 6. Convert transaction date to date format
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
# 7. Create transaction month
df["transaction_month"] = df["transaction_date"].dt.to_period("M").astype(str)
# 8. Write processed transaction data
df.to_csv(
    "data/processed/transactions_processed.csv",
    index=False
)

print("\nProcessed transactions saved successfully!")