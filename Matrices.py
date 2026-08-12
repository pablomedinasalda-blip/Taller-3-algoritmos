import os
def limpiar_terminal():
    os.system("cls")
limpiar_terminal()

# PUNTO 3
# Operaciones entre matrices
# Primera Parte
# Función para ingresar una matriz.
# -----------------------------------------------------
def ingresar_matriz():

    # Se inicia un ciclo para validar el número de filas.
    while True:

        try:

            # Se solicita la cantidad de filas.
            filas = int(input("Ingrese la cantidad de filas: "))

            # Se verifica que sea mayor que cero.
            if filas > 0:
                break

            # Si es menor o igual a cero se muestra un mensaje.
            else:
                print("La cantidad de filas debe ser mayor que cero.")

        # Si el usuario escribe letras se captura el error.
        except ValueError:

            print("Debe ingresar un numero entero.")


    # Se inicia un ciclo para validar las columnas.
    while True:

        try:

            # Se solicita la cantidad de columnas.
            columnas = int(input("Ingrese la cantidad de columnas: "))

            # Se verifica que sea mayor que cero.
            if columnas > 0:
                break

            else:
                print("La cantidad de columnas debe ser mayor que cero.")

        except ValueError:

            print("Debe ingresar un numero entero.")


    # Se crea una lista vacía donde se almacenará la matriz.
    matriz = []


    # Se recorren las filas.
    for i in range(filas):

        # Se crea una lista para guardar la fila actual.
        fila = []

        # Se recorren las columnas.
        for j in range(columnas):

            # Se valida el dato ingresado.
            while True:

                try:

                    # Se solicita el número.
                    numero = int(input(f"Ingrese el elemento [{i}][{j}]: "))

                    # Se guarda el número en la fila.
                    fila.append(numero)

                    # Se termina el ciclo.
                    break

                except ValueError:

                    print("Debe ingresar un numero entero.")

        # Se agrega la fila completa a la matriz.
        matriz.append(fila)

    # La función devuelve la matriz creada.
    return matriz


# -----------------------------------------------------
# Función para mostrar una matriz.
# -----------------------------------------------------
def mostrar_matriz(matriz):

    # Si la matriz no existe se informa al usuario.
    if matriz is None:

        print("La matriz aun no ha sido creada.")

    else:

        # Se recorren las filas de la matriz.
        for fila in matriz:

            # Se imprime la fila.
            print(fila)

# Función para sumar dos matrices.
# -----------------------------------------------------
def sumar_matrices(matriz_a, matriz_b):

    # Se verifica que ambas matrices existan.
    if matriz_a is None or matriz_b is None:

        print("Primero debe ingresar las matrices A y B.")

        return None

    # Se obtiene la cantidad de filas.
    filas = len(matriz_a)

    # Se obtiene la cantidad de columnas.
    columnas = len(matriz_a[0])

    # Se crea la matriz donde se almacenará el resultado.
    matriz_c = []

    # Se recorren las filas.
    for i in range(filas):

        # Se crea una nueva fila.
        fila = []

        # Se recorren las columnas.
        for j in range(columnas):

            # Se suma cada posición de ambas matrices.
            suma = matriz_a[i][j] + matriz_b[i][j]

            # Se agrega el resultado a la fila.
            fila.append(suma)

        # Se agrega la fila completa.
        matriz_c.append(fila)

    # Se devuelve la matriz resultado.
    return matriz_c


# -----------------------------------------------------
# Función para restar dos matrices.
# -----------------------------------------------------
def restar_matrices(matriz_a, matriz_b):

    # Se verifica que ambas matrices existan.
    if matriz_a is None or matriz_b is None:

        print("Primero debe ingresar las matrices A y B.")

        return None

    # Se obtiene la cantidad de filas.
    filas = len(matriz_a)

    # Se obtiene la cantidad de columnas.
    columnas = len(matriz_a[0])

    # Se crea la matriz donde se guardará el resultado.
    matriz_d = []

    # Se recorren las filas.
    for i in range(filas):

        # Se crea una nueva fila.
        fila = []

        # Se recorren las columnas.
        for j in range(columnas):

            # Se realiza la resta B - A.
            resta = matriz_b[i][j] - matriz_a[i][j]

            # Se agrega el resultado a la fila.
            fila.append(resta)

        # Se agrega la fila a la matriz.
        matriz_d.append(fila)

    # Se devuelve la matriz resultante.
    return matriz_d

# Programa Principal
# -----------------------------------------------------

# Se inicializan las matrices.
matriz_a = None
matriz_b = None
matriz_c = None
matriz_d = None

# Se inicia el menú.
while True:

    # Se limpia la terminal.
    limpiar_terminal()

    # Se muestra el menú.
    print("====================================")
    print("     MENU DE MATRICES")
    print("====================================")
    print("1. Llenar la Matriz A")
    print("2. Llenar la Matriz B")
    print("3. Calcular Matriz C = A + B")
    print("4. Calcular Matriz D = B - A")
    print("5. Mostrar una matriz")
    print("6. Salir")
    print("====================================")

    # Se valida la opción del usuario.
    while True:

        try:

            opcion = int(input("Seleccione una opcion: "))

            if 1 <= opcion <= 6:
                break

            else:
                print("Ingrese una opcion valida.")

        except ValueError:

            print("Debe ingresar un numero.")

    # -----------------------------------------------------
    # Opción 1
    # -----------------------------------------------------
    if opcion == 1:

        print("\nIngreso de la Matriz A")

        matriz_a = ingresar_matriz()

        input("\nPresione ENTER para continuar...")

    # -----------------------------------------------------
    # Opción 2
    # -----------------------------------------------------
    elif opcion == 2:

        print("\nIngreso de la Matriz B")

        matriz_b = ingresar_matriz()

        input("\nPresione ENTER para continuar...")

    # -----------------------------------------------------
    # Opción 3
    # -----------------------------------------------------
    elif opcion == 3:

        if matriz_a is None or matriz_b is None:

            print("Debe ingresar primero las matrices A y B.")

        elif len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):

            print("Las matrices deben tener el mismo tamaño.")

        else:

            matriz_c = sumar_matrices(matriz_a, matriz_b)

            print("La matriz C fue calculada correctamente.")

        input("\nPresione ENTER para continuar...")

    # -----------------------------------------------------
    # Opción 4
    # -----------------------------------------------------
    elif opcion == 4:

        if matriz_a is None or matriz_b is None:

            print("Debe ingresar primero las matrices A y B.")

        elif len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):

            print("Las matrices deben tener el mismo tamaño.")

        else:

            matriz_d = restar_matrices(matriz_a, matriz_b)

            print("La matriz D fue calculada correctamente.")

        input("\nPresione ENTER para continuar...")

    # -----------------------------------------------------
    # Opción 5
    # -----------------------------------------------------
    elif opcion == 5:

        print("\n¿Que matriz desea mostrar?")
        print("1. Matriz A")
        print("2. Matriz B")
        print("3. Matriz C")
        print("4. Matriz D")

        while True:

            try:

                mostrar = int(input("Seleccione una opcion: "))

                if 1 <= mostrar <= 4:
                    break

                else:
                    print("Opcion invalida.")

            except ValueError:

                print("Debe ingresar un numero.")

        if mostrar == 1:

            print("\nMATRIZ A")
            mostrar_matriz(matriz_a)

        elif mostrar == 2:

            print("\nMATRIZ B")
            mostrar_matriz(matriz_b)

        elif mostrar == 3:

            print("\nMATRIZ C")
            mostrar_matriz(matriz_c)

        elif mostrar == 4:

            print("\nMATRIZ D")
            mostrar_matriz(matriz_d)

        input("\nPresione ENTER para continuar...")

    # -----------------------------------------------------
    # Opción 6
    # -----------------------------------------------------
    elif opcion == 6:

        print("\nGracias por utilizar el programa.")

        break
print("Nueva funcion agregada al proyecto de matrices")