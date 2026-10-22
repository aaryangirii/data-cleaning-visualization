from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ROOT = Path(__file__).resolve().parent
source = ROOT / "outputs/clean_customers.csv"
if not source.exists():
    raise FileNotFoundError("Run task_2_clean_data.py first.")
data = pd.read_csv(source)
out = ROOT / "outputs"
sns.set_theme(style="whitegrid")
charts = [
    ("monthly_spend_distribution.png", lambda ax: sns.histplot(data=data, x="monthly_spend", bins=8, kde=True, ax=ax), "Monthly Customer Spend"),
    ("spend_by_membership.png", lambda ax: sns.barplot(data=data, x="membership", y="monthly_spend", errorbar=None, ax=ax), "Average Spend by Membership"),
    ("visits_vs_spend.png", lambda ax: sns.scatterplot(data=data, x="visits_per_month", y="monthly_spend", hue="membership", ax=ax), "Visits vs Monthly Spend")
]
for filename, draw, title in charts:
    fig, ax = plt.subplots(figsize=(8, 5))
    draw(ax); ax.set_title(title); fig.tight_layout()
    fig.savefig(out / filename, dpi=150); plt.close(fig)
print("Charts saved in", out)
