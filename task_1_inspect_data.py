from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent
data = pd.read_csv(ROOT / "data/messy_customers.csv")
print("\nFirst rows:\n", data.head().to_string(index=False))
print(f"\nShape: {data.shape}")
print("\nColumn types:\n", data.dtypes)
print("\nMissing values:\n", data.isna().sum())
print("\nDuplicate rows:", data.duplicated().sum())
print("\nNumeric summary:\n", data.describe().round(2))
