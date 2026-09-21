# Practica grupo3 - Alineacion de cadenas
# Programacion dinamica


def crear_matriz(cadena1, cadena2, penalidad_diferencia, penalidad_gap):
    filas = len(cadena1) + 1
    columnas = len(cadena2) + 1

    matriz = [[0 for j in range(columnas)] for i in range(filas)]

    # Primera columna: se agregan gaps en la segunda cadena
    for i in range(1, filas):
        matriz[i][0] = i * penalidad_gap

    # Primera fila: se agregan gaps en la primera cadena
    for j in range(1, columnas):
        matriz[0][j] = j * penalidad_gap

    # Se llena el resto de la matriz
    for i in range(1, filas):
        for j in range(1, columnas):
            if cadena1[i - 1] == cadena2[j - 1]:
                diagonal = matriz[i - 1][j - 1]
            else:
                diagonal = matriz[i - 1][j - 1] + penalidad_diferencia

            arriba = matriz[i - 1][j] + penalidad_gap
            izquierda = matriz[i][j - 1] + penalidad_gap

            matriz[i][j] = min(diagonal, arriba, izquierda)

    return matriz


def mostrar_matriz(cadena1, cadena2, matriz):
    encabezado = ["-"] + list(cadena2)
    filas = ["-"] + list(cadena1)

    ancho = max(4, max(len(str(valor)) for fila in matriz for valor in fila) + 2)

    print("\nMatriz resultante:\n")
    print(" " * ancho + "".join(f"{letra:>{ancho}}" for letra in encabezado))

    for i in range(len(matriz)):
        valores = "".join(f"{matriz[i][j]:>{ancho}}" for j in range(len(matriz[i])))
        print(f"{filas[i]:>{ancho}}{valores}")


def reconstruir_alineacion(cadena1, cadena2, matriz, penalidad_diferencia, penalidad_gap):
    i = len(cadena1)
    j = len(cadena2)
    alineada1 = []
    alineada2 = []
    operaciones = []

    while i > 0 or j > 0:
        # Coincidencia o sustitucion
        if i > 0 and j > 0:
            costo = 0 if cadena1[i - 1] == cadena2[j - 1] else penalidad_diferencia

            if matriz[i][j] == matriz[i - 1][j - 1] + costo:
                alineada1.append(cadena1[i - 1])
                alineada2.append(cadena2[j - 1])

                if cadena1[i - 1] != cadena2[j - 1]:
                    operaciones.append(
                        f"Sustituir {cadena1[i - 1]} por {cadena2[j - 1]}"
                    )

                i -= 1
                j -= 1
                continue

        # Borrado de un caracter de la primera cadena
        if i > 0 and matriz[i][j] == matriz[i - 1][j] + penalidad_gap:
            alineada1.append(cadena1[i - 1])
            alineada2.append("-")
            operaciones.append(f"Borrar {cadena1[i - 1]}")
            i -= 1
            continue

        # Insercion de un caracter de la segunda cadena
        if j > 0:
            alineada1.append("-")
            alineada2.append(cadena2[j - 1])
            operaciones.append(f"Insertar {cadena2[j - 1]}")
            j -= 1

    alineada1.reverse()
    alineada2.reverse()
    operaciones.reverse()

    return "".join(alineada1), "".join(alineada2), operaciones


def resolver_alineacion(cadena1, cadena2, penalidad_diferencia=1, penalidad_gap=1):
    matriz = crear_matriz(cadena1, cadena2, penalidad_diferencia, penalidad_gap)
    mostrar_matriz(cadena1, cadena2, matriz)

    alineada1, alineada2, operaciones = reconstruir_alineacion(
        cadena1, cadena2, matriz, penalidad_diferencia, penalidad_gap
    )

    print("\nResultado:")
    print("Cadena 1:", alineada1)
    print("Cadena 2:", alineada2)
    print("Costo minimo:", matriz[len(cadena1)][len(cadena2)])

    print("\nOperaciones encontradas:")
    if len(operaciones) == 0:
        print("No se necesitan cambios.")
    else:
        for numero, operacion in enumerate(operaciones, 1):
            print(f"{numero}. {operacion}")


print("ALINEACION DE CADENAS - PROGRAMACION DINAMICA")
print("Las penalidades se dejan en 1 para que la prueba sea facil de revisar.\n")

cadena1 = input("Ingrese la primera cadena: ").strip().upper()
cadena2 = input("Ingrese la segunda cadena: ").strip().upper()

if cadena1 == "" or cadena2 == "":
    print("Las dos cadenas deben tener al menos un caracter.")
else:
    resolver_alineacion(cadena1, cadena2)
