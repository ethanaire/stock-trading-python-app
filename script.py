import requests
import csv
import os
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

LIMIT = 1000 

def run_stock_job(): 
    url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
    response = requests.get(url)
    tickers = []
    
    data = response.json()
    
    if 'results' in data:
        for ticker in data['results']:
            tickers.append(ticker)
    else:
        print("API error:", data)
        exit(1)  # or handle differently
    
    
    while 'next_url' in data:
        print('requesting next page', data['next_url'])
        response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
        time.sleep(12) # Make 1 request every 12 seconds 
        data = response.json()
        print(data)
        
        if 'results' not in data:  
            print("API error:", data)
            break  # stop the loop if API fails
    
        for ticker in data['results']:
            tickers.append(ticker)
    
    example_ticker = {
        "ticker": "AAPL",
        "name": "Apple Inc.",
        "market": "stocks",
        "locale": "us",
        "primary_exchange": "XNAS",
        "type": "CS",
        "active": True,
        "currency_name": "usd",
        "cik": "0000320193",
        "composite_figi": "BBG000B9XRY4",
        "share_class_figi": "BBG001S5N8V8",
        "last_updated_utc": "2024-06-20T00:00:00Z"
    }
    
    # Write tickers to CSV
    fieldnames = list(example_ticker.keys())
    output_csv = 'tickers.csv'
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for t in tickers:
            # Only write the fields in csv_columns, fill missing keys with empty string
            row = {key: t.get(key, '') for key in fieldnames}
            writer.writerow(row)
    print(f"Wrote {len(tickers)} rows to {output_csv}")

if _name_ == '__main__': 
    run_stock_job()
