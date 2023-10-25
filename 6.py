def contar_lineas_de_codigo(archivo_path):
    try:
        with open(archivo_path, "r") as archivo:
            lineas = archivo.readlines()
            lineas_de_codigo = 0
            for linea in lineas:
                linea = linea.strip() 
                if linea and not linea.startswith("#"):
                    lineas_de_codigo += 1

            return lineas_de_codigo
    except FileNotFoundError:
        print("El archivo no se encontró. Asegúrese de que la ruta del archivo es correcta.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
def main():
    archivo_path = input("Ingrese la ruta del archivo .py: ")
    if archivo_path.endswith(".py"):
        lineas_de_codigo = contar_lineas_de_codigo(archivo_path)
        if lineas_de_codigo is not None:
            print(f"Número de líneas de código en {archivo_path}: {lineas_de_codigo}")
    else:
        print("El archivo no es un archivo .py válido.")
if __name__ == "__main__":
    main()
    