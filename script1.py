import requests
import pandas as pd
from bs4 import BeautifulSoup

# Create a session to store cookies
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.nseindia.com/"
})

# Step 1: Visit the NSE site once to get cookies
session.get("https://www.nseindia.com", timeout=10)

# Step 2: Fetch NIFTY 50 data
url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
resp = session.get(url, timeout=10)
data = resp.json()

# Step 3: Extract stock list
records = []
for item in data["data"]:
    records.append({
        "symbol": item["symbol"],
        "companyName": item["meta"]["companyName"] if "meta" in item and "companyName" in item["meta"] else item["symbol"],
        "sector": item.get("sector", "Unknown")
    })

# Step 4: Save to CSV
df = pd.DataFrame(records)
df.to_csv("nifty50_stocks.csv", index=False)
print(" nifty50_stocks.csv created successfully with", len(df), "stocks")
