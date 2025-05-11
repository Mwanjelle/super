import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
if response.status_code == 200:
    data = response.json()
    price_usd = data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price (USD):", price_usd)
else:
    print("\nFailed to fetch data from API")
