# Ejercicio Bingo
# ENTRADA

import random
# Definimos los números que pueden ser sorteados y mesclamos su orden de forma aleatorea
numeros_sorteados = list(range(1, 51))
random.shuffle(numeros_sorteados)

# Definimos dos variables para acceder al valor de fila y columna del carton
cantidad_filas = 5
cantidad_columnas = 5

# Definimos una matriz con 25 elementos no repetidos en un rango de 1 y 50 
numeros_carton = random.sample(range(1, 51), 25)
carton = [numeros_carton[i:i+5] for i in range(0, 25, 5)]

# Variable que permite pasar al siguiente número a buscar
numero_encontrado = False

gano = False

# PROCESO / SALIDA

# Se le muestra el carton al usuario
print("Tu cartón es: \n")
for fila in carton:
    for columna in fila:
        print(columna, end = " ")
    print()
print()

# Bucle que recorre las 50 posiciones de la lista numeros_sorteados tomando el elemento de cada posicion
for numero in numeros_sorteados:
    print(f"Numero sorteado : {numero}")
    numero_encontrado = False
    # Bucle anidado que se fija si, el nro tomado en el ciclo anterior esta o no en la posicion fila y columna del cartón 
    for posicion_filas in range(cantidad_filas):
        for posicion_columna in range(cantidad_columnas):
            # En caso de que el nro tomado se encuentre en la posición se remplazara por un cero y le dira al usuario, ¡Lo Tenés!
            # Si no lo encuentra lo seguira buscando en las otras posiciones y en caso de que no lo tenga se lo comunicara al usuario
            # Además se muestra el cartón actualizado al usuario
            if carton[posicion_filas][posicion_columna] == numero:
                print("¡Lo Tenés! \n")
                carton[posicion_filas][posicion_columna] = 0
                for fila in carton:
                    for columna in fila:
                        print(columna, end = " ")
                    print()
                print()
                numero_encontrado = True
                # Sale del bucle
                break
        # Si el nro se encontro en alguna columna de la fila, sale del bucle, para buscar un nuevo nro
        if numero_encontrado == True:
            break

    if numero_encontrado == False:
        print("No lo tenés \n")

# Bucle para saber si gano
    for posicion_filas in range(cantidad_filas):
        for posicion_columna in range(cantidad_columnas):
            if carton[posicion_filas][posicion_columna] == 0:
                gano == True
            else:
                gano == False
                break
        if gano == False:
            break

if gano == True:
    print("¡Bingo!")
