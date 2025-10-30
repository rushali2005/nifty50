import requests
import pandas as pd
import time

# Load NIFTY 50 stock list
nifty_df = pd.read_csv("nifty50_stocks.csv")

# Create session for consistent access
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.nseindia.com/"
})

# Get initial cookies
session.get("https://www.nseindia.com", timeout=10)

momentum_data = []

for symbol in nifty_df["symbol"]:
    try:
        url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol}"
        resp = session.get(url, timeout=10)
        data = resp.json()
        
        # Extract prices safely
        current_price = data["priceInfo"]["lastPrice"]
        prev_close = data["priceInfo"]["previousClose"]
        intraday_change = current_price - prev_close
        
        momentum_data.append({
            "symbol": symbol,
            "sector": nifty_df.loc[nifty_df["symbol"] == symbol, "sector"].values[0],
            "current_price": current_price,
            "prev_close": prev_close,
            "intraday_change": intraday_change
        })
        print(f" Fetched {symbol}")

        time.sleep(1)  # polite delay
    except Exception as e:
        print(f" Skipping {symbol}: {e}")
        continue

# Convert to DataFrame
momentum_df = pd.DataFrame(momentum_data)

# Group by sector to calculate average intraday change
if not momentum_df.empty:
    sector_momentum = (
        momentum_df.groupby("sector")["intraday_change"]
        .mean()
        .reset_index()
        .sort_values(by="intraday_change", ascending=False)
    )
    print("\n📈 Sector Momentum Ranking:")
    print(sector_momentum)
    sector_momentum.to_csv("sector_momentum.csv", index=False)
    print("\n Saved sector_momentum.csv successfully.")
else:
    print(" No valid data collected.")
