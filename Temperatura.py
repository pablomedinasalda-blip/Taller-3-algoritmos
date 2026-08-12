import os
def limpiar_terminal():
    os.system("cls")
limpiar_terminal()

# PUNTO 1
# Conversión de temperaturas de Celsius a Fahrenheit

# Lista con las temperaturas en grados Celsius
temp_celsius = [0, 20, 37, 40, 35, 27, 45]

# Se utiliza map() junto con una función lambda para convertir
# cada temperatura a grados Fahrenheit.
# Fórmula:
# Fahrenheit = (Celsius * 9/5) + 32

temp_fahrenheit = list(map(lambda temperatura: (temperatura * 9/5) + 32, temp_celsius))

# Se muestra la lista convertida
print("Temperaturas convertidas a Fahrenheit:")
print(temp_fahrenheit)

# Se ordenan las temperaturas de mayor a menor
temperaturas_ordenadas = sorted(temp_fahrenheit, reverse=True)

# Se imprime el resultado con el formato solicitado
print("\nLas temperaturas convertidas a grados Fahrenheit son:")

for temperatura in temperaturas_ordenadas:
    print(f"--- {temperatura}")

# PUNTO 2
# Conversión de Fahrenheit a Celsius
# -----------------------------------------

# Lista de tuplas con el nombre de la ciudad y la temperatura
# registrada en grados Fahrenheit.

temp_fahrenheit = [
    ("Envigado", 78.8),
    ("Itagui", 57.2),
    ("La Estrella", 86),
    ("Caldas", 53.6)
]

# Se utiliza map() y lambda para convertir las temperaturas
# de Fahrenheit a Celsius.
# La estructura conserva el nombre de la ciudad.

temp_celsius = list(
    map(
        lambda ciudad: (
            ciudad[0],
            round((ciudad[1] - 32) * 5 / 9, 1)
        ),
        temp_fahrenheit
    )
)

# Se muestra la nueva lista convertida

print("Temperaturas convertidas a Celsius:")

print(temp_celsius)

# Se ordenan las ciudades de mayor a menor temperatura
# usando la temperatura en Fahrenheit.

ciudades_ordenadas = sorted(
    temp_fahrenheit,
    key=lambda ciudad: ciudad[1],
    reverse=True
)

print("\nTemperaturas en Fahrenheit (ordenadas de mayor a menor):")

# Se muestra cada ciudad con su temperatura convertida a Celsius
for ciudad, fahrenheit in ciudades_ordenadas:

    celsius = round((fahrenheit - 32) * 5 / 9, 1)

    print(f"--- {ciudad}: {celsius} °C")