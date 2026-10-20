# Sales Performance Analysis (Python)

A small pandas project that cleans an order dataset, calculates revenue,
compares regions and identifies the top orders.

## What the script does
1. **Inspect**: shape, missing values, data types, duplicates
2. **Clean**: removes duplicate orders, fills missing discounts with 0 (assumption: no discount recorded = no discount)
3. **Validate**: keeps only rows with units > 0 and unit_price >= 0
4. **Calculate**: revenue = units × unit_price × (1 − discount)
5. **Summarise**: orders, units, total revenue and average order revenue by region
6. **Benchmark**: flags orders above the portfolio average revenue
7. **Export**: saves `sales_clean.csv` and `regional_summary.csv`

## Key findings
| Region | Orders | Units | Revenue | Avg order revenue |
|--------|--------|-------|---------|-------------------|
| East   | 3 | 7 | 222,400 | 74,133 |
| West   | 2 | 5 | 121,600 | 60,800 |
| North  | 1 | 1 | 15,000  | 15,000 |

- East generates the most revenue, driven mainly by order 7 (160,000).
- The top 3 orders are 7, 2 and 6.
- 1 duplicate row (order 4) was removed; 1 missing discount was filled with 0.

## Tools
Python, pandas, NumPy

## How to run
```bash
pip install pandas numpy
python sales_performance.py
```

## Next steps
- Load the data from a CSV instead of an inline DataFrame
- Add charts (matplotlib) for revenue by region
