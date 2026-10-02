import pandas as pd

df = pd.read_csv("sales_raw.csv")
df = df.drop_duplicates()
df["product"] = df["product"].str.strip().str.capitalize()


def fix_date(d):
    d = str(d).strip()
    if "/" in d:
        return pd.to_datetime(d, format="%d/%m/%Y").strftime("%Y-%m-%d")
    return pd.to_datetime(d, format="%Y-%m-%d").strftime("%Y-%m-%d")


df["date"] = df["date"].apply(fix_date)
df["price"] = df["price"].fillna(df.groupby("product")["price"].transform("max"))
df = df.dropna(subset=["quantity", "price"])
df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(int)
df["total"] = df["quantity"] * df["price"]
df.to_csv("sales_clean.csv", index=False)
print(df)