import pandas as pd

# 1. Read processed customer data
customers = pd.read_csv("data/processed/customers_processed.csv")

# 2. Read processed transaction data
transactions = pd.read_csv("data/processed/transactions_processed.csv")

# 3. Join customers and transactions
customer_transactions = transactions.merge(
    customers,
    on="customer_id",
    how="inner"
)

# 4. Display joined data
print("Customer Transaction Data:")
print(customer_transactions)

# 5. Save joined data
customer_transactions.to_csv(
    "data/processed/customer_transactions.csv",
    index=False
)

print("\nJoined records:", len(customer_transactions))
print("Customer transaction ETL completed successfully!")
# 6. Calculate customer-level transaction summary
customer_summary = customer_transactions.groupby("customer_id").agg(
    transaction_count=("transaction_id", "count"),
    total_amount=("amount", "sum")
).reset_index()

# 7. Display customer summary
print("\nCustomer Transaction Summary:")
print(customer_summary)

# 8. Save customer summary
customer_summary.to_csv(
    "data/curated/customer_transaction_summary.csv",
    index=False
)

print("\nCustomer summary saved successfully!")
# 9. Source vs processed reconciliation

raw_transactions = pd.read_csv("data/raw/transactions.csv")

raw_count = len(raw_transactions)
processed_count = len(transactions)

raw_amount = raw_transactions["amount"].sum()
processed_amount = transactions["amount"].sum()

print("\nSource vs Processed Reconciliation:")
print("Raw transaction count:", raw_count)
print("Processed transaction count:", processed_count)
print("Raw transaction amount:", raw_amount)
print("Processed transaction amount:", processed_amount)

if raw_count == processed_count and raw_amount == processed_amount:
    print("Reconciliation Status: PASSED")
else:
    print("Reconciliation Status: FAILED")