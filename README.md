#Lab 2 — Data Collection & Pre-Processing (PROG8245)

Author: Albright Maduka
Course: PROG8245 – Machine Learning Programming

A 12-step data engineering roadmap applied to a real-world e-commerce dataset is included in this repository.  End-to-end work will be demonstrated, including feature engineering, mini-aggregation, cleaning, transformations, profiling, ingestion, and a serialization checkpoint.

Datasets

Primary sales data: data/1000 Sales Records.csv
Source: https://excelbianalytics.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/

Synthetic customers: data/synthetic_customers.csv
(Exported locally; provides customer_id, coupon_code, shipping_city.)

The workflow loads both files into DataFrames, standardizes headers (lower-snake case), then builds typed Python objects (Transaction) and a tidy analysis DataFrame.

In the bash terminal
python -m venv venv
pip install -r requirements.txt

12-Step

1. Hello, Data! – load both CSVs; preview with .head()

2. Pick the Right Container- dict vs namedtuple vs sets(1–2 sentences)

3. Implement Functions & Data Structure

4. Bulk Loaded – load_transactions(...) -> list[Transaction] 

5. Quick Profiling – min/mean/max price

6. Spotting the Grime – deliberately inject dirty values ("N/A", negatives, NaN)

7. Cleaning – find via Boolean-style list comps; fix via clean(price_median); re-verify

8. Transformations – compute discount_pct, net_price, revenue; build transaction_key; assemble analysis DataFrame

9. Feature Engineering – days_since_purchase (via property), order_year, order_month

10. Mini-Aggregation – revenue by city (pure Python + pandas)

11. Serialization Checkpoint – saving to JSON

12. Soft Interview Reflection – short paragraph on how the class encapsulates data and behaviour

