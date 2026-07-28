import pandas as pd
from datetime import date
from scraper import scrape_lift

results = scrape_lift("JNB", "CPT")
df = pd.DataFrame(results)

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

today = pd.Timestamp(date.today())
cutoff = today + pd.Timedelta(days=30)
df = df[(df["date"] > today) & (df["date"] <= cutoff)]

df["price_numeric"] = df["price"].str.replace("R", "").str.replace(",", "").str.strip().astype(float)
df = df.sort_values("price_numeric")

print("Cheapest flight:")
print(df.iloc[0])

df.to_csv("results.csv", index=False)
print("\nSaved all results to results.csv")