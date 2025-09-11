# Ejercicio Bingo
import random
cantidad_filas = 5
cantidad_columnas = 5
numeros_carton = random.sample(range(1, 51), 25)
carton = [numeros_carton[i:i+5] for i in range(0, 25, 5)]
numero_sorteado = 0
carton_en_cero = True
no_gana = True

# Se le muestra el carton al usuario
print("Tu carton es:")
for fila in carton:
    for columna in fila:
        print(columna, end = " ")
    print()
    

# En caso de que la condición no gana sea cierta se ejecuta el bucle
while no_gana:
    # Genera número aleatoreo entre 1 y 50
    numero_sorteado = random.randint(1, 50)
    # Muestra el nro por pantalla
    print(f"Número sorteado {numero_sorteado} \n")

    for posicion_fila in range(cantidad_filas):
        for posicion_columna in range(cantidad_columnas):
            # Se fija si la posicion coincide con el valor
            if carton[posicion_fila][posicion_columna] == numero_sorteado:
                print("¡Lo tenés! \n")
                # Si es cierto se cambia el valor de dicha posición por 0
                carton[posicion_fila][posicion_columna] = 0
                # Se muestra el carton actualizado
                for fila in carton:
                    for columna in fila:
                        print(columna, end = " ")
                    print()

# Verificacion para saber si gano o no
    for posicion_fila in range(cantidad_filas):
        for posicion_columna in range(cantidad_columnas):
            # Si se encuentra en alguna posición un elemento distinto de 0, carton_en_cero va a ser igual a falso
            # para que se siga ejecutando el bucle while, hasta que el carton sea igaul a cero
            if carton[posicion_fila][posicion_columna] != 0:
                carton_en_cero = False
                break
            else:
                carton_en_cero = True

        # En caso de que el carton no este en 0
        if carton_en_cero == False:
            # Sale del bucle para seguir jugando
            break
        else:
            # Si no, no_gana va a ser falso para salir del bucle
            no_gana = False

print()
# Una ves sale del bucle se muestra el mensaje ¡Bingo! segido del carton con toas sus posiciones en cero para que el usuario sepa que gano
print("¡Bingo!")
for fila in carton:
    for columna in fila:
        print(columna, end = " ")
    print()