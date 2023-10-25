def guardar_tabla_multiplicar(n):
    if 1 <= n <= 10:
        with open(f"tabla-{n}.txt", "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla de multiplicar del {n} guardada en tabla-{n}.txt")
    else:
        print("El número debe estar entre 1 y 10.")

def mostrar_tabla_multiplicar(n):
    if 1 <= n <= 10:
        try:
            with open(f"tabla-{n}.txt", "r") as archivo:
                contenido = archivo.read()
                print(f"Tabla de multiplicar del {n}:\n{contenido}")
        except FileNotFoundError:
            print(f"El archivo tabla-{n}.txt no existe.")
    else:
        print("El número debe estar entre 1 y 10.")

def mostrar_linea_tabla_multiplicar(n, m):
    if 1 <= n <= 10:
        try:
            with open(f"tabla-{n}.txt", "r") as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= 10:
                    if m <= len(lineas):
                        linea = lineas[m - 1]
                        print(f"Línea {m} de la tabla de multiplicar del {n}: {linea}")
                    else:
                        print(f"No existe una línea {m} en el archivo tabla-{n}.txt.")
                else:
                    print("El número 'm' debe estar entre 1 y 10.")
        except FileNotFoundError:
            print(f"El archivo tabla-{n}.txt no existe.")
    else:
        print("El número 'n' debe estar entre 1 y 10.")

def menu():
    while True:
        print("Menú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            n = int(input("Ingrese un número (1-10) para guardar su tabla de multiplicar: "))
            guardar_tabla_multiplicar(n)
        elif opcion == "2":
            n = int(input("Ingrese un número (1-10) para mostrar su tabla de multiplicar: "))
            mostrar_tabla_multiplicar(n)
        elif opcion == "3":
            n = int(input("Ingrese un número (1-10) para seleccionar la tabla de multiplicar: "))
            m = int(input("Ingrese el número de línea a mostrar: "))
            mostrar_linea_tabla_multiplicar(n, m)
        elif opcion == "4":
            print("¡Cierre!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
if __name__ == "__main__":
    menu()