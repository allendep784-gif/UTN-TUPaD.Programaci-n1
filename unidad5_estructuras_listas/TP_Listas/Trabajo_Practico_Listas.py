# EJERCICIO 1

print("EJERCICIO 1")

# Definición de variable
multiplos_de_cuatro = []

# Entrada/Proceso
for numero in range(1, 101):
    if numero % 4 == 0:
        multiplos_de_cuatro.append(numero)

# Salida

print("Lista con los multiplos de cuatro:")
# Bucle que muestra todos los valores almacenados en la lista seguido de una coma, en caso de ser el último valor la como no se imprimira
for i in range(len(multiplos_de_cuatro)):
    if multiplos_de_cuatro[i] == multiplos_de_cuatro[-1]:
        print(multiplos_de_cuatro[i])
    else:
        print(multiplos_de_cuatro[i], end=", ")

print()


# EJERCICIO 2
print("EJERCICIO 2")

# Definición de variables
lista_ejercicio_2 = ["Milanesa", True, 3.14, 51, "P"]

# Salida
print("Penultima posicón de la lista:")
print(lista_ejercicio_2[-2])
print()


# EJERCICIO 3
print("EJERCICIO 3")

# Deinición de variable
lista_ejercicio_3 = []

# Proceso
lista_ejercicio_3.append("Milanesa")
lista_ejercicio_3.append("Napolitana")
lista_ejercicio_3.append("Helado")

# Salida

print("Lista con los tres valores agregados:")
# Bucle que muestra todos los valores almacenados en la lista seguido de una coma, en caso de ser el último valor la como no se imprimira
for i in range(len(lista_ejercicio_3)):
    if lista_ejercicio_3[i] == lista_ejercicio_3[-1]:
        print(lista_ejercicio_3[i])
    else:
        print(lista_ejercicio_3[i], end=", ")

print()


# EJERCICIO 4
print("EJERCICIO 4")

# Definisión variable
animales = ["Perro", "gato", "Conejo", "Pez"]

# Proceso 
animales[-3] = "loro"
animales[-1] = "oso"

# Salida 

print("Lista con el segundo y último valor remplazados:")
# Bucle que muestra todos los valores almacenados en la lista seguido de una coma, en caso de ser el último valor la como no se imprimira
for i in range(len(animales)):
    if animales[i] == animales[-1]:
        print(animales[i])
    else:
        print(animales[i], end=", ")

print()


# EJERCICIO 5
print("Ejercicio 5")

print("En este programa se define una lista con diferentes valores enteros. Luego con las funciosnes .remove(max(numero))")
print("Elimina el número más grande de la lista.")
print()


#EJERCICIO 6
print("Ejercicio 6")

# Definición variable
numeros_10_a_30 = []

# Proceso
# Bucle que va del 10 al 30 de 5 en 5
for i in range(10, 31, 5):
    numeros_10_a_30.append(i)

# Salida

print("Los dos primeros valores de la lista son: ")

# Bucle que recorre del 0 al 1 para imprimir los dos primeros valores de numeros_10_a_30
for i in range(2):

# En caso de que la poición de la lista actual tenga el mismo valor de la posición a la que queremos llegar imprimimos ese valor
# sin coma, caso contrario imprimimos el valor seguido de una coma 
    if numeros_10_a_30[i] == numeros_10_a_30[1]:
        print(numeros_10_a_30[i])
    else:
            print(numeros_10_a_30[i], end=", ")
print()


# EJERCICIO 7
print("Ejercicio 7")

# Definición de variables
autos = ["sedan", "polo", "suran", "gol"]

# Proceso
autos[1] = "Ford"
autos[2] = "Pagani"

# Salida
print(autos)


# EJERCICIO 8
print("Ejercicio 8")

# Definicón de variable
dobles = []

# Proceso
dobles.append(10)
dobles.append(20)
dobles.append(30)

# Salida
# Bucle que muestra eldoble de 5, 10 y 15
for posicion in range(len(dobles)):
    print(f"Doble de {dobles[posicion] // 2}: {dobles[posicion]} ")
print()


# EJERCICIO 9 
print("Ejercicio 9 \n")

# Definición de variable
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

# Proceso
# Agregamos el valor "jugo" a la tercer sub-lusta
compras[-1].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

# Salida
# Bucle anidado para mostrar los productos llevados por cada cliente en forma de lista
for cliente in range(len(compras)):
    print(f"Cliente {cliente + 1}:", end= " ")
    for productos in range(len(compras[cliente])):
        if compras[cliente][productos] == compras[cliente][-1]:
            print(compras[cliente][productos])
        else:
            print(compras[cliente][productos], end=", ")

print()


# EJERCICIO 10
print("Ejercicio 10")

# Definición variables
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Bucle for que imprime todos los elementos de la lista.

# Utilizo la funcción isintance  que me permite verificar si algunos de sus elementos es una lista en caso de que asi sea 
# se ejecutara lo que está dentro del if

# La funcion isinstance resive dos prametros el elemento a verificar y el tipo de dato, también podemos pasarle una tupla
# con varios tipos para que pueda comparar por ejemplo isinstance(elemento, (int, float, true)) en caso de que elemento sea
# de tipo int, float o true devolvera verdadero, caso contrario devolvera falso 

for elemento in range(len(lista_anidada)):
    if isinstance(elemento, list):
        print("[")
        for elemento_sub_lista in range(len(lista_anidada[elemento])):
            if lista_anidada[elemento][elemento_sub_lista] == lista_anidada[elemento][-1]:
                print(lista_anidada[elemento][elemento_sub_lista], end="], ")
            else:
                print(lista_anidada[elemento][elemento_sub_lista], end=", ")
    else:
        if lista_anidada[elemento] == lista_anidada[-1]:
            print(lista_anidada[elemento])
        else:
            print(lista_anidada[elemento], end=", ")
