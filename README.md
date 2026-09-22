# Telecom Data Engineering

A Python-based ETL pipeline for processing customer and transaction data, performing data-quality validation, transforming and joining datasets, generating customer-level summaries, and performing source-to-target reconciliation.

## Technologies Used

* Python
* Pandas
* SQL concepts
* CSV
* PowerShell
* VS Code
* Git
* GitHub

## Project Structure

```text
telecom-data-engineering/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   └── transactions.csv
│   │
│   ├── processed/
│   │   ├── customers_processed.csv
│   │   ├── customer_rejects.csv
│   │   ├── customer_transactions.csv
│   │   └── transactions_processed.csv
│   │
│   └── curated/
│       └── customer_transaction_summary.csv
│
├── docs/
│
├── notebooks/
│
├── src/
│   ├── customer_etl.py
│   ├── transaction_etl.py
│   └── customer_transaction_etl.py
│
└── README.md
```

## ETL Pipeline

```text
Raw Customer Data
       |
       v
customer_etl.py
       |
       +----> Valid Customers
       |
       +----> Rejected Customers
       |
       v
Processed Customer Data


Raw Transaction Data
       |
       v
transaction_etl.py
       |
       v
Processed Transaction Data


Processed Customers
       +
Processed Transactions
       |
       v
customer_transaction_etl.py
       |
       +----> Join Customer + Transaction Data
       |
       +----> Customer-level Aggregation
       |
       +----> Source-to-Target Reconciliation
       |
       v
Curated Customer Transaction Summary
```

## Data Quality Checks

The pipeline performs the following validations:

### Customer Data

* Missing-value validation
* Duplicate customer detection
* Separation of valid and rejected records

### Transaction Data

* Missing-value validation
* Transaction amount validation
* Transaction status validation

## Customer ETL Results

The source customer file contained 12 records.

```text
Total records   : 12
Valid records   : 10
Rejected records: 2
```

The rejected records contained data-quality issues such as a duplicate customer and missing customer information.

## Transaction ETL Results

The transaction pipeline processed 15 transactions successfully.

```text
Raw transaction count       : 15
Processed transaction count : 15
```

No missing values, invalid transaction amounts, or invalid transaction statuses were found in the transaction dataset.

## Customer Transaction Summary

The final curated dataset contains customer-level transaction metrics:

* `customer_id`
* `transaction_count`
* `total_amount`

Example:

```text
C001 → 2 transactions → 1950.50
C004 → 2 transactions → 3700.00
C006 → 1 transaction  → 3100.00
```

## Reconciliation

The pipeline performs source-to-target reconciliation by comparing transaction counts and transaction amounts.

```text
Raw transaction count       : 15
Processed transaction count : 15

Raw transaction amount       : 21203.25
Processed transaction amount : 21203.25

Reconciliation Status        : PASSED
```

## Key ETL Concepts Practiced

* Extracting data from CSV files
* Data transformation using Pandas
* Data-quality validation
* Handling missing values
* Duplicate detection
* Rejecting invalid records
* Joining datasets
* Aggregating transaction data
* Creating curated datasets
* Source-to-target reconciliation

## How to Run

From the project root directory:

```powershell
python src/customer_etl.py
python src/transaction_etl.py
python src/customer_transaction_etl.py
```

## Day 1 Outcome

Successfully built and executed an end-to-end Python ETL pipeline that transforms raw customer
