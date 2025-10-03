# EJERCICIO 1
def imprimir_hola_mundo():
    print("Hola Mundo")



# EJERCICIO 2
def saludar_usuario(nombre):
    # Variable que almacenara el saludo a devolver
    saludo_devolver = "Hola " + nombre
    return saludo_devolver



# EJERCICIO 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")



# EJERCICIO 4
def calcular_area_circulo(radio):
    # Variable que almacena el valor de PI (aproximado)
    PI = 3.14   
    # Variable que almacena el area del circulo
    area = 0
    # Se calcula el valor del area
    area = PI * (radio ** 2)
    # Retorna el area
    return area


def calcular_perimetro_circulo(radio):
    # Variable que almacena el valor de PI (aproximado)
    PI = 3.14
    # variable que almacenara el perímetro del circulo
    perimetro = 0
    # Se calcula y almecena el perimetro del círculo con la (formula 2 X PI X r)
    perimetro = 2 * PI * radio
    # Retorna el perímetro
    return perimetro



# EJERCICIO 5
# Función que convierte los segundos a hora
def segundos_a_horas(segundos):
    # Variable que almacena los segundos en horas
    horas_totales = 0

    # Utilizando la regla de 3 simple convertimos los segundos en minutos
    # Formula utilizada: (segundos X 1h) / 3600s
    horas_totales = (segundos * 1) / 3600
    return horas_totales



# EJERCICIO 6
def tabla_multiplicar(numero):
    for multiplicador in range(1, 11):
        print(f"{numero} X {multiplicador} = {numero * multiplicador}" )


# EJERCICIO 7
def operaciones_basicas(a, b):
    # Se definen y asigna valor a las variables que almacenaran la suma, resta, multiplicación y división de dos números
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    # Tuppla que almacenara los resultados
    tupla_resultado = (suma, resta, multiplicacion, division) 
    # Retorna tupla
    return tupla_resultado


# EJERCICIO 8
# Funcion que calcula el índice de masa corporal de una persona
def calcular_imc(peso, altura):
    # Variable que almacena el IMC de una persona
    imc = (altura ** 2) / peso
    imc = round(imc, 2)
    # Retorna el IMC
    return imc


# EJERCICIO 9
# Función que transforma los grados celcius a fharenheit
def celsius_a_fahrenheit(celsius):
    # Variable que almacenara los grados fahrenheit 
    fahrenheit = 0
    # Usamos regla de 3 simple para calcular los f°
    # Formula = (celsius * 33.8) / 1
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit


# EJERCICIO 10
#Función que calcula el promedio de 3 números
def calcular_promedio(a, b, c):
    # variable que almacena la suma de los números
    suma = a + b + c
    # variable que almacena el promedio
    promedio = suma / 3
    return promedio


# ===========================================================================================================================


# ALGORITMO PRINCIPAL
# se definen 4 variables una almacena el nombre del usuario, otra el apellido, edad y residencia
nombre_usuario = ""
apellido_usuario = ""
residencia_usuario = ""
eadad_usuario = 0
# Variable que almacenara un saludo con un nombre
saludo_personalizado = ""

# Se definen 3 variables una para ingresar el radio de un círclo, otra para almacenar el area calculada
# y la última para almacenar el perímetro calculado
radio_circulo = 0
area_circulo = 0
perimetro_circulo = 0

# Se define 2 variables una almecena una cantidad x de segundos y la otra su equivalencia en horas
segundos_ingresado = 0
segundos_en_horas = 0

# Variable que almacena un número para mostrar su tabla
multiplicando = 0

# 3 variables que se utilizaran para realizar operaciones básicas y  para calcular el promedio
# también se define una tuppla que almacenara sus resultados
numero1 = 0
numero2 = 0
numero3 = 0
resultados_básicos = ()

# Variable que almacena un promedio
promedio = 0

# 2 variables una almecena el peso en kg y la otra almacena la altura en metros
peso_kg = 0
altura_metros = 0
indice_masa_corporal = 0

# 2 variables una representa los grado celcius y la otra los grados fsreheint
grados_celsius = 0
grados_fahrenheit = 0

# ===========================================================================================================================
# Entrada / Salida

# Ejercicio 1
print("Ejercicio 1")
# Se llama a la funcion imprimir hola mundo si argumentos ya que solo imprimira un mensaje
imprimir_hola_mundo()
print()



# EJERCICIO 2
print("Ejercicio 2") 
# Se le pide al usuario que ingrese su nombre
nombre_usuario = input("Ingrese su nombre: ").capitalize()
# A la variable saludo personalizado le asignams el valor que retorna la función saludar_usuario
saludo_personalizado = saludar_usuario(nombre_usuario)
# Se muestra el saludo por pantalla
print(saludo_personalizado)
print()



# EJERCICIO 3
print("Ejercicio 3")
# Se le pide al usuario que ingrese su información personal
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
eadad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese el nombre del lugar de su residencia: ")
informacion_personal(nombre_usuario, apellido_usuario, eadad_usuario, residencia_usuario)
print()


# EJERCICIO 4
print("Ejercicio 4")
# Se pide que el usuario ingrese el radio de un círculo para calcular su aréa y perímetro
radio_circulo = float(input("Ingrese el radio del círculo: "))
# Se le asigna a la variable el area calculada
area_circulo = calcular_area_circulo(radio_circulo)
# Se asigna a la variable el perímetro calculado
perimetro_circulo = calcular_perimetro_circulo(radio_circulo)
# Se muestra por pantalla los resultados
print(f"El aréa del circulo es: {area_circulo}")
print(f"El perímetro del circulo es: {perimetro_circulo}")
print()


# EJERCICIO 5
print("Ejercicio 5")
# Se pide al usuario que ingrese una cantidad de segundos
segundos_ingresado = float(input("Ingrese una cantidad de segundos: "))
# En la siguiente variable se almacena los segundos ingresados en horas
segundos_en_horas = segundos_a_horas(segundos_ingresado)
# Mostramos la equivalencia
print(f"{segundos_ingresado}s equivalen a {segundos_en_horas} horas")
print()


# EJERCICIO 6
print("Ejercicio 6")
# Se le pide al usuario que ingrese un número
multiplicando = int(input("Ingrese un número para conocer su tabla: "))
# Se llama a la función y se le pasa un número como parametro para saber su tabla
tabla_multiplicar(multiplicando)
print()


# EJERCICIO 7
print("Ejercicio 7")
# Se le pide al usuario que ingrese dos números
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
# Se le  asigna a la tupla la tupla retornada por la funcón
resultados_básicos = operaciones_basicas(numero1, numero2)
# Bucle que muestra cada valor almacenado en la tupla
for indice in range(4):
    if indice == 0: 
        print(f"{numero1} + {numero2} = {resultados_básicos[indice]}")
    elif indice == 1:
        print(f"{numero1} - {numero2} = {resultados_básicos[indice]}")
    elif indice == 2:
        print(f"{numero1} X {numero2} = {resultados_básicos[indice]}")
    elif indice == 3:
        print(f"{numero1} / {numero2} = {resultados_básicos[indice]}")
print()



# EJERCICIO 8
print("Ejercicio 8")
# Se le pide al usuario que ingrese su altura en etros y su peso en kg
peso_kg = float(input("Ingrese su peso en KG: "))
altura_metros = float(input(" Ingrese su altura en metros: "))
# Se asigna a la variable indice_ masa_corporal el imc
indice_masa_corporal = calcular_imc(peso_kg, altura_metros)
print(f"Su índice de masa corporal es de: {indice_masa_corporal} Kg/m2")
print()



# EJERCICIO 9
print("Ejercicio 9")
# Se pide al usuario que ingrese los grados celsius
grados_celsius = float(input("Ingrese los grados celsius: "))
# Se almacena en la variable grados Fahrenheith el equivalente de grados celsius en fahrenheith
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(f"{grados_celsius}°C equivalen a {grados_fahrenheit}°F")
print()



# EJERCICIO 10
print("Ejercicio 10")
# Se le pide al usuario que ingrese 3 números
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
numero3 = float(input("Ingrese un último número: "))
# A la variable promedio se le almacena el promedio de los tres números ingresados
promedio = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio de {numero1}, {numero2}, y {numero3} es de: {promedio}")