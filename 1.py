import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status() 

        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al consultar la API de CoinDesk: {e}")
        return None

def main():
    try:
        cantidad_bitcoins = float(input("Ingresar la cantidad de bitcoins que posee: "))
        
        precio_bitcoin = obtener_precio_bitcoin()
        if precio_bitcoin is not None:
            costo_actual_usd = cantidad_bitcoins * precio_bitcoin
            print(f"El costo actual de {cantidad_bitcoins:.4f} Bitcoins en USD es: ${costo_actual_usd:,.4f}")
    except ValueError:
        print("Ingresar una cantidad válida de Bitcoins.")
    
if __name__ == "__main__":
    main()
