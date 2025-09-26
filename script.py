import requests
import csv
import os
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file
import snowflake.connector
from datetime import datetime

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 1000 
DS = '2025-09-26'

def run_stock_job(): 
    DS = datetime.now().strftime('%Y-%m-%d')
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
            ticker['ds'] = DS
            tickers.append(ticker)
    
    example_ticker = {
        'ticker': 'ZWS', 
        'name': 'Zurn Elkay Water Solutions Corporation', 
        'market': 'stocks', 
        'locale': 'us', 
        'primary_exchange': 'XNYS', 
        'type': 'CS', 
        'active': True, 
        'currency_name': 'usd', 
        'cik': '0001439288', 
        'composite_figi': 'BBG000H8R0N8', 	
        'share_class_figi': 'BBG001T36GB5', 	
        'last_updated_utc': '2025-09-11T06:11:10.586204443Z',
        'ds': '2025-09-25'
    }
    
    fieldnames = list(example_ticker.keys())
    
    # Load to Snowflake instead of CSV
    load_to_snowflake(tickers, fieldnames)
    print(f'Loaded {len(tickers)} rows to Snowflake')

if _name_ == '__main__': 
    run_stock_job()
