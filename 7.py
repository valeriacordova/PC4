import requests
import sqlite3
def obtener_tipo_cambio_senat():
    try:
        response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat")
        response.raise_for_status()

        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error al consultar el tipo de cambio de SUNAT: {e}")
        return None

def crear_tabla_sunat_info():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha DATE,
            compra_usd DECIMAL,
            venta_usd DECIMAL,
            compra_eur DECIMAL,
            venta_eur DECIMAL,
            compra_gbp DECIMAL,
            venta_gbp DECIMAL
        )
    ''')
    conn.commit()
    conn.close()

def guardar_datos_sunat_info(data):
    if data:
        fecha = data["date"]
        compra_usd = data["compra_usd"]
        venta_usd = data["venta_usd"]
        compra_eur = data["compra_eur"]
        venta_eur = data["venta_eur"]
        compra_gbp = data["compra_gbp"]
        venta_gbp = data["venta_gbp"]

        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sunat_info (fecha, compra_usd, venta_usd, compra_eur, venta_eur, compra_gbp, venta_gbp) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (fecha, compra_usd, venta_usd, compra_eur, venta_eur, compra_gbp, venta_gbp))
        conn.commit()
        conn.close()
