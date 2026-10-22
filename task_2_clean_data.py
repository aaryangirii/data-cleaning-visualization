from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent
data = pd.read_csv(ROOT / "data/messy_customers.csv")
before = len(data)
data = data.drop_duplicates().copy()
for col in ["age", "monthly_spend", "visits_per_month"]:
    data[col] = data[col].fillna(data[col].median())
data["city"] = data["city"].fillna(data["city"].mode().iloc[0])
# These bounds are examples for this practice dataset, not universal rules.
data["age"] = data["age"].clip(18, 100)
data["monthly_spend"] = data["monthly_spend"].clip(upper=data["monthly_spend"].quantile(.95))
data["visits_per_month"] = data["visits_per_month"].clip(lower=0)
out = ROOT / "outputs"
out.mkdir(exist_ok=True)
data.to_csv(out / "clean_customers.csv", index=False)
print(f"Rows before cleaning: {before}; after cleaning: {len(data)}")
print("Missing values after cleaning:\n", data.isna().sum())
print("Saved:", out / "clean_customers.csv")
