# EJERCICIO 1
print("Ejercicio 1")
# Bucle para imprimir de forma creciente los nros comprendidos entre 0 y 10, estos incluidos
for i in range(0, 101):
    print(i)
print()


# EJERCICIO 2
print("Ejercicio 2")

# ENTRADA
# Definimos una variable para que el usuario ingrese un número entero positivo o negativo
numero_original_1 = int(input("Ingrese un número entero: "))

# Definimos una variable que almacena el valor de la variable original para asi poder realizar los calculos necesarios sin
# afectar el valor original 
numero_entero_1 = numero_original_1

# Definimos la variable que almacenara la cantidad de dígitos
cantidad_digitos = 0

# PROCESO
# Mientras la variable sea distinta a cero, (posea al menos un dígito) dividira el valor entre 10 y se quedara con la parte entera
# de la división, posteriormente se incrementara el contador de dígitos
while numero_entero_1 != 0:
    # Condicion para saber si el nro es positivo o negativo en caso de que sea negativo dividimos el valor por -10 
    # para convertirlo a positivo
    if numero_entero_1 < 0:
        numero_entero_1 = numero_entero_1 // -10
        cantidad_digitos += 1
    else:
        numero_entero_1 = numero_entero_1 // 10
        cantidad_digitos += 1

# SALIDA
print(f"El número {numero_original_1}, tiene {cantidad_digitos} dígitos.", "\n")


# EJERCICIO 3
print("Ejercicio 3")

# Enrada
# Definimos una variale para que el usuario ingrese un número
numero_entero_2 = int(input("Ingrese un número: "))

# Defino dos variabl, una para almacenar el nro ingresado más grande y otra para almacenar el nro ingresado más chico
numero_mayor_1 = numero_entero_2
numero_menor_1 = numero_entero_2

# Defino variable para almacenar la suma
suma = 0

# Bucle para validar los datos ingresados
while numero_mayor_1 == numero_menor_1:
    numero_entero_2 = int(input("Ingrese otro número: "))
    if numero_entero_2 > numero_mayor_1:
        numero_mayor_1 = numero_entero_2
    elif numero_entero_2 < numero_menor_1:
        numero_menor_1 = numero_entero_2
    else:
        print("No puede ingresar dos numero iguales")

# PROCESO
# Bucle que suma todos los numeros comprendidos entre los valores ingresados por el usuario sin tener en cuenta a estos
for i in range(numero_menor_1 + 1, numero_mayor_1):
    suma += i

# SALIDA
print(f"La suma de los números comprendidos entre {numero_menor_1} y {numero_mayor_1} sin contar estos es de: {suma}", "\n")


# EJERCICIO 4
print("Ejercicio 4")

numero_entero_3 = 0
suma = 0

# Bucle para validar el valor ingresado
while numero_entero_3 == 0:
    numero_entero_3 = int(input("Ingrese un número entero: "))
    if numero_entero_3 == 0:
        print("Debe ingresar un número distinto de cero")
    else:
        suma += numero_entero_3

# PROCESO
# Bucle para sumar todos los valores que ingrese el usuario hasta que ingrese el nro 0
while numero_entero_3 != 0:
    numero_entero_3 = int(input("Ingrese otor valor para realizar la suma o un cero para ver el resultado de esta: "))
    if numero_entero_3 != 0:
        suma += numero_entero_3

# SALIDA
print(f"La suma de los valores ingresados es de: {suma}")
print()


# EJERCICIO 5
print("Ejercicio 5 \n")

import random

numero_aleatoreo = random.randint(1, 9) 
numero_usuario = 0
intentos = 0

# PROCESO
print("                     ADIVINA EL NÚMERO \n")
print("Bienvenido/a a ADIVINA EL NÚMERO, en este juego deberas ingresar un número entre 0 y 9.")
print("Para ganar debes adivinar el número y se mostraran los intentos que utilizaste para adivinarlo ")


# Bucle anidado que verifica si el valor ingresado está en el rango permitido y si adivino o no el número
# cada vez que ingrese un número se incrementara en  la variable que cuenta los intentos
while True:
    while True:
        numero_usuario = int(input("Esperando valor: \n"))
        if numero_usuario < 0 or numero_usuario > 9:
            print("Debes ingresar un valor que se encuentre entre 0 y 9 \n")
        else:
            break
    # Si el numero ingresado es igual al numero aleatoreo  saldra drl bucle si no, debera seguiir intentando
    intentos += 1
    if numero_aleatoreo == numero_usuario:
        break

# SALIDA
print("Felizitaciones has conseguido adivinar el número!!!!")
print(f"Número a adivinar: {numero_aleatoreo}")
print(f"Intentos utilizados {intentos}")
print()


# EJERCICIO 6
print("Ejercicio 6")

# Bucle que imprime en forma decreciente los números pares desde el 100 al 0
# En este caso puse con paso -2 pero, también podria poner la siguiente condición dentro del bucle (if i % 2 == 0:) 
# si se cumple la condición imprimiria i
for i in range(100, -1, -2):
    if i == 0:
        print(i)
    else:
        print(i, end=", ")
print()

# EJERCICIO 7
print("Ejercicio 7 \n")
numero_entero = 0
suma = 0

# Bucle para verificar valor ingresado:
while True:
    numero_entero = int(input("Ingrese un número entero positivo: "))
    if numero_entero > 0:
        break
    else:
        print("Debes ingresar un número entero positivo")

# PROCESO
# Bucle para realizar la sumatoria de los numeros comprendidos entre 0 y el nuúmero ingresado por el usuario
for i in range(numero_entero + 1):
    suma += i

# SALIDA
print(f"La suma de los números comprendidos entre 0 y {numero_entero} incluyendo a estos, es de: {suma}")


# EJERCICIO 8
print("Ejercicio 8 \n")

lista_numeros = []
numero_entero = 0
cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0

# Bucle para ingresar los 100 valores a la lista
for i in range(4):
    numero_entero = int(input("Ingrese un número entero: "))
    lista_numeros.append(numero_entero)

# PROCESO
# Bucle para ver cuántos de los números ingresados son pares, impares, positivos y negativos
for i in range(4):
    if lista_numeros[i] % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
    
    if lista_numeros[i] > 0:
        cantidad_positivos += 1
    else:
        cantidad_negativos += 1

# SALIDA
print(f"Cantidad de números ingresados:", "\n", f"Pares: {cantidad_pares}", "\n", f"Impares: {cantidad_impares}")
print( f" Positivos: {cantidad_positivos}", "\n", f"Negativos: {cantidad_negativos}")


# EJERCICIO 9
print(" Ejercicio 9 \n")

# Importo una función que me permite calcular la media
import statistics
from statistics import mean

# Definición de variables
lista_numero = []
numero_entero = 0
media = 0

# Bucle para darle valor a la lista
for i in range(4):
    numero_entero = int(input("Ingrese un número entero: "))
    lista_numero.append(numero_entero)

# PROCESO
media = mean(lista_numero)

# SALIDA
print()
print("Los números ingresados fueron: ")
for i in range(4):
    print(lista_numero[i])
print()

print(f"La media estos números es de: {media} ")
print()


# EJERCICIO 10
print("Ejercicio 10 \n")

# Definisión de las variables a utilizar
numero_original = 0
numero_condicion = 0
numero_invertido = 0
auxiliar = 0

# Mensaje para que el usuario sepa lo que debe ingresar
print("Ingrese un número con 2 dígitos como mínimo, para invertir el orden sus números")

# Bucle para verificar el valor de la variable
while True:
    numero_original = int(input("Esperando valor: "))
    print()
    if numero_original > 0:
        # Si al dividir el número por 10 su parte entera es diferente de 1 significa que tiene más de un digíto
        if ((numero_original // 10) != 0):
            break
        else:
            print("Debe ingresar un número con 2 digitos como mínimo")
            print()
    elif numero_original < 0:
        # Si al dividir el número por -10 su parte entera es diferente de 1 significa que tiene más de un digíto
        if ((numero_original // -10) != 0):
            break
        else:
            print("Debe ingresar un número con 2 digitos como mínimo")

# PROCESO
# Inicializo la variable que me permite contolar la condicón
numero_condicion = numero_original

# En el caso de que el valor de numero_condicion sea negativo, 
# lo pasaremos a positivo para poder invertir el orden de sus números (Si no lo hcemos, el programa se traba)
# luego de esto lo volveremos a pasar a positivo
# FORMULA A UTILIZAR (EJEMPLO): -125 / -1 = 125 ------> 125 / -1 = -125
if numero_condicion < 0:
    numero_condicion = numero_condicion / -1

# Bucle para innvertir los números del número original
while numero_condicion != 0:
    auxiliar = numero_condicion % 10
    numero_condicion = numero_condicion // 10
    numero_invertido = (numero_invertido * 10) + auxiliar

# Si el valor original era negativo, volvera a se negativo
if numero_original < 0:
    numero_invertido = numero_invertido / -1

# SALIDA
print(F"Número original: {numero_original}")
print(f"Número al revés: {numero_invertido}")