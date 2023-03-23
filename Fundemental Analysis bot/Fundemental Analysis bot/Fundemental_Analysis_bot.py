
import requests
import json

#symbol = 'AAPL' # Symbol for Apple Inc.
#data = yf.download(symbol, start='2010-01-01', end='2023-02-21')

symbol = 'AAPL' # Symbol for Apple Inc.
url = f'https://financialmodelingprep.com/api/v3/financials/income-statement/{symbol}?apikey=6773f916da46be1f54613e01994d476d'

response = requests.get(url)
data = json.loads(response.text)

#Extracting data
income_statement = data['financials']

