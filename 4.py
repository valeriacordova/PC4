import json
data = {
    "time": {
        "updated": "Oct 24, 2023 05:16:00 UTC",
        "updatedISO": "2023-10-24T05:16:00+00:00",
        "updateduk": "Oct 24, 2023 at 06:16 BST"
    },
    "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
    "chartName": "Bitcoin",
    "bpi": {
        "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "34,426.3834",
            "description": "United States Dollar",
            "rate_float": 34426.3834
        },
        "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "28,766.4106",
            "description": "British Pound Sterling",
            "rate_float": 28766.4106
        },
        "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "33,536.3237",
            "description": "Euro",
            "rate_float": 33536.3237
        }
    }
}
archivo_txt = "bitcoin_price.txt"
with open(archivo_txt, 'w') as archivo:
    json.dump(data, archivo, indent=4)
print(f"Los datos de precio de Bitcoin se han guardado en '{archivo_txt}'.")