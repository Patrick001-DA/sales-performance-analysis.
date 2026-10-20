#project: sales performance
#Goal: clean a small dataset, calculate revenue, compare regions, identify top orders and export the results.


import numpy as np

import pandas as pd


raw = pd.DataFrame({

 "order_id": [1, 2, 3, 4, 4, 6, 7],

 "region": ["East", "West", "East", "North", "North", "West", "East"],

 "units": [2, 1, 3, 1, 1, 4, 2],

 "unit_price": [15000, 80000, 12000, 15000, 15000, 12000, 80000],

 "discount": [0.00, 0.05, 0.10, 0.00, 0.00, 0.05, np.nan]

})


# 1. Inspect

print(raw.shape)

print(raw.isna().sum())
print(raw.describe())
print(raw.dtypes)
print(raw.columns)
print(raw.duplicated().sum())
#2. clean
data=raw.drop_duplicates().copy()
#2.1  discounts are assumed to be 0
data["discount"] = data["discount"].fillna(0)
# 3. Validate

data= data.loc[(data["units"] > 0) & (data["unit_price"] >= 0)].copy()

data["revenue"] = data["units"] * data["unit_price"] * (1 - data["discount"])

# 4. Summarise

regional = (

 data.groupby("region", as_index=False)

 .agg(orders=("order_id", "nunique"),

 units=("units", "sum"),

 revenue=("revenue", "sum"),

 avg_order_revenue=("revenue", "mean"))

 .sort_values("revenue", ascending=False)

)

# 5. Add a portfolio-level benchmark

portfolio_average = data["revenue"].mean()

data["above_average"] = data["revenue"] > portfolio_average

print(regional)
print(data[["order_id", "revenue", "above_average"]])

print(data.nlargest(3, "revenue"))

# 6. Export

data.to_csv("sales_clean.csv", index=False)

regional.to_csv("regional_summary.csv", index=False)

