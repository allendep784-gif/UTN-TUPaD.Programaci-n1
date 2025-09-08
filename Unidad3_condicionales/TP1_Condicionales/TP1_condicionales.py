# Ejercicio 1
print("Ejercicio 1 \n")
edad_1 = 0
edad_1 = int(input("Ingrese su edad: "))

if edad_1 > 18:
    print("Es mayor de edad")

print("\n")

# Ejercicio 2
print("Ejercicio 2 \n")
nota_usuario = 0
nota_usuario = float(input("Ingrese su nota: "))

if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("\n")

# Ejercicio 3
print("Ejercicio 3 \n")
numero_ingresado = 0
numero_ingresado = int(input("Ingrese un número par: "))

if numero_ingresado % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("\n")

# Ejercicio 4
print("Ejercicio 4 \n")
edad_2 = 0
edad_2 = int(input("Ingrese su edad: "))

if edad_2 < 12:
    print("Eres un/una niño/a")
elif edad_2 >= 12 and edad_2 < 18:
    print("Eres un adolecente")
elif edad_2 >= 18 and edad_2 < 30:
    print("Eres un/una adulto/a joven")
elif edad_2 >= 30:
    print("Eres un/una adulto/a")

print("\n")

# Ejercicio 5
print("Ejercicio 5 \n")
contrasenia = ""
contrasenia = input("Ingrese una contraseña que tenga entre 8 y 14 carcteres: ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("\n")

# Ejercicio 6
print("Ejercicio 6 \n")
import random
import statistics
from statistics import mean
from statistics import mode
numeros_aleatoreos = []
moda = 0
media = 0
mediana = 0

numeros_aleatoreos = [2.0,2.0,2.0,3.0,3.0,4.0,5.0,5.0,7.0,8.0]
moda = mode(numeros_aleatoreos)
media = mean(numeros_aleatoreos)
mediana = statistics.median(numeros_aleatoreos)
print(f"media: {media}, mediana: {mediana}, moda: {moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
print()

# Ejercicio 7
print("Ejercicio 7 \n")
frase_palabra = input("Ingrese una frase o palabra: ")
letras = list(frase_palabra)

if letras[-1] == "a" or letras[-1] == "A":
    print(f"{frase_palabra}!")
elif letras[-1] == "e" or letras[-1] == "E":
    print(f"{frase_palabra}!")
elif letras[-1] == "i" or letras[-1] == "I":
    print(f"{frase_palabra}!")
elif letras[-1] == "o" or letras[-1] == "O":
    print(f"{frase_palabra}!")
elif letras[-1] == "u" or letras[-1] == "U":
    print(f"{frase_palabra}!")
else:
    print(frase_palabra)

print()

# Ejercicio 8
print("Ejercicio 8 \n")
nombre_1 = input("Ingrese su nombre: ")
nombre_final_1 = ""
opcion = 0

print("presione: ")
print("1)_ Para escribir su nombre en mayúscula")
print("2)_ Para escribir su nombre en minúsculas")
print("3)_ Para escribir la primer letra de su nombre en mayúscula\n")

opcion = int(input("Esperando elección: "))
print()

if opcion == 1:
    nombre_final_1 = nombre_1.upper()
elif opcion == 2:
    nombre_final_1 = nombre_1.lower()
elif opcion == 3:
    nombre_final_1 = nombre_1.title()
else:
    print("Valor ingresado no válido")

print(nombre_final_1)
print()

# Ejercicio 9
print("Ejercicio 9 \n")
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3:
    print("La magnitud del terremoto fue: Muy Leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("La magnitud del terremoto fue: Leve ")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("La magnitud del terremoto fue: Moderado")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("La magnitud del terremoto fue: Fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("La magnitud del terremoto fue: Muy Fuerte")
elif magnitud_terremoto >= 7:
    print("La magnitud del terremoto fue: Extremo")

print()

# #Ejercicio 10
print("Ejercicio 10 \n")
hemisferio = input("Ingrese en que hemisferio se encuentre (Norte/Sur): ").capitalize()
mes = input("Ingrese el nombre del mes en el que se encuentre: ").lower()
dia = int(input("Ingrese el número del día en el que se encuentre: "))

if hemisferio == "Norte":
    if mes == "enero":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en Invierno")
        else:
            print("Día inválido")
    elif mes == "febrero":
        if dia >= 1 and dia <= 29:
            print("Se encuentra en Invierno")
        else:
            print("Día inválido")
    elif mes == "marzo":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en Invierno")
        elif dia >= 21 and dia <= 31:
            print("se encuentra en Primevera")
        else:
            print("Día inválido")
    elif mes == "abril":
        if dia >= 1 and dia <= 30:
            print("Se encuentra en primavera")
        else:
            print("Día inválido")
    elif mes == "mayo":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en primavera")
        else:
            print("Día inválido")
    elif mes == "junio":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en Primavera")
        elif dia >= 21 and dia <= 30:
            print("se encuentra en Verano")
        else:
            print("Día inválido")
    elif mes == "julio":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en Verano")
        else:
            print("Día Invalido")
    elif mes == "agosto":
        if dia >= 1 and dia <= 30:
            print("Se encuentra en Verano")
        else:
            print("Día Invalido")
    elif mes == "septiembre":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en Verano")
        elif dia >= 21 and dia <= 30:
            print("se encuentra en Otoño")
        else:
            print("Día inválido")
    elif mes == "octubre":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en Otoño")
        else:
            print("Día Invalido")
    elif mes == "noviembre":
        if dia >= 1 and dia <= 30:
            print("Se encuentra en Otoño")
        else:
            print("Día Invalido")
    elif mes == "diciembre":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en otoño")
        elif dia >= 21 and dia <= 31:
            print("se encuentra en Invierno")
        else:
            print("Día inválido")
elif hemisferio == "Sur":
    if mes == "enero":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en Verano")
        else:
            print("Día inválido")
    elif mes == "febrero":
        if dia >= 1 and dia <= 29:
            print("Se encuentra en Verano")
        else:
            print("Día inválido")
    elif mes == "marzo":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en Verano")
        elif dia >= 21 and dia <= 31:
            print("se encuentra en Otoño")
        else:
            print("Día inválido")
    elif mes == "abril":
        if dia >= 1 and dia <= 30:
            print("Se encuentra en Otoño")
        else:
            print("Día inválido")
    elif mes == "mayo":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en Otoño")
        else:
            print("Día inválido")
    elif mes == "junio":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en Otoño")
        elif dia >= 21 and dia <= 30:
            print("se encuentra en Invierno")
        else:
            print("Día inválido")
    elif mes == "julio":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en Invierno")
        else:
            print("Día Invalido")
    elif mes == "agosto":
        if dia >= 1 and dia <= 30:
            print("Se encuentra en Invierno")
        else:
            print("Día Invalido")
    elif mes == "septiembre":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en Invierno")
        elif dia >= 21 and dia <= 30:
            print("se encuentra en Primavera")
        else:
            print("Día inválido")
    elif mes == "octubre":
        if dia >= 1 and dia <= 31:
            print("Se encuentra en Primavera")
        else:
            print("Día Invalido")
    elif mes == "noviembre":
        if dia >= 1 and dia <= 30:
            print("Se encuentra en Primavera")
        else:
            print("Día Invalido")
    elif mes == "diciembre":
        if dia >= 1 and dia <= 20:
            print("Se encuentra en Primavera")
        elif dia >= 21 and dia <= 31:
            print("se encuentra en Verano")
        else:
            print("Día inválido")