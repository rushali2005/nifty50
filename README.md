Project: NIFTY 50 Intraday Momentum Analysis

Objective
Analyze the intraday momentum of NIFTY 50 stocks by fetching live data from NSE India and ranking sectors based on their average intraday price movement.

Steps Performed
Script 1 – Data Fetching (script1.py)
Fetches the latest list of NIFTY 50 stocks from NSE India’s API.
Saves the data (symbol, company name, sector) to nifty50_stocks.csv.

Script 2 – Momentum Analysis (script2.py)
Fetches live price info (current & previous close) for each stock.
Calculates intraday change and averages it per sector.
Outputs sector-wise ranking in sector_momentum.csv.

Technologies Used
Python
Requests
Pandas
JSON / REST APIs

Output Files
nifty50_stocks.csv → List of current NIFTY 50 stocks
sector_momentum.csv → Ranked sector momentum data

