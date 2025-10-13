# Se llama a las funciones a utilizar en el código
from validar import *
from validar_ejercicio_9 import *


#================================================================================================================


#EJERCICIO 1
# Lista de frutas con sus precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Se agrega nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


#================================================================================================================


# EJERCICIO 2
# Se acturalizan valores del diciionario del ejercicio 1
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


#================================================================================================================


# EJERCICIO 3
# Se actualiza valores del diccionario para crear una lista de las frutas sin precio
precios_frutas['Naranja'] = 0
precios_frutas['Melón'] = 0
precios_frutas['Banana'] = 0
# Se definer lista para almacenar las claves que no tengan valor
clave_sin_valor = []

# Se reccorre cada par del diccionario para asignarle a la lista las claves que no tienen valor
for clave, valor in precios_frutas.items():
    if valor == 0:
        clave_sin_valor.append(clave)


#================================================================================================================


# EJERCICIOO 4
# Diccionario que almacenara los contactos del usuario con sus respectivos nro telefónicos
contactos = {}
# Variable que almacena el nombre del contacto del usuario
conocido = ""
# Variable que almacenarael nro telefónico del contacto
telefono = 0
# Lista para verificar que no se ingresen más de una vez el mismo número
numeros_telefonos = []

print("EJERCICIO 4")
# Bucle parta que el usuario agregue 5 contactos
for contacto in range(1, 6):
    print(f"Contacto {contacto}:")
    conocido = validar_nombre(contactos)

    while True:
        telefono = entero_positivo()
# Se verifica que no se haya ingresado antes este número de telefono, en caso de ser verdadero se verifica que 
# el número sea válido
        if not telefono in numeros_telefonos:
            if len(telefono) == 10:
                numeros_telefonos.append(telefono)
                contactos[conocido] = telefono
                break
            else:
                print("Error, el número debe contener 10 dígitos \n")
        else:
            print("Error, este número de telefono es de otro contacto \n")

# Se le pide al usuario que ingrese el nombre de un contacto para mostrar su nro telefónico
print("Ingrese el nombre de un contacto para ver sunúmero telefónico: ")
conocido = input("Esperando nombre: ").strip().capitalize()

if conocido in contactos:
    print("Numero de telefono: ")
    print(contactos[conocido])
else:
    print(f"{conocido} no es un contacto agendado.")


#================================================================================================================


# EJERCICIO 5
# Variable que almacenara lafrase ingresada por el usuario
frase = ""
# Variable que almacenara cada palabra de la frase
palabras = []
# Diccionario que contara la cantidad de veces que sale una palabra
contar_palabra = {}
# Set que mostrara todas las palabras sin repetir
palabras_sin_repetir = ()

print("EJERCICIO 5")
# Se le pide al usuario que ingrese una frase
frase = input("Ingrese una frase: ")
print()
# Se separan las palabras y se asignan a una lista
palabras = frase.split()
# Se almacena en un Set todas las palabras pero sin repetir
palabras_sin_repetir = set(palabras)

# Bucle para crear el diccionario que contendra cuantas veces se repite la palabra
for palabra in palabras:
    if not palabra in contar_palabra:
        contar_palabra[palabra] = contador_palabra(palabra, palabras)

print(f"Frase ingresada: {frase}")
print() 

print("Palabras sin repetir de la frase ingresada: ")
for palabra in palabras_sin_repetir:
    print(f"- {palabra}")
print()

if len(palabras) == 1:
    print(f"La palabra {palabras[0]} aparece 1 ves")
else:
    print("Conteo de las palabras ingresadas: ")
    for clave, valor in contar_palabra.items():
        print(f"- {clave}: {valor}")
print()


#================================================================================================================


# EJERCICIO 6
# Variable que almacenara el nombre del alumno
nombre_alumno = ""
# Variable para que se ingrese la nota del alumno
nota_alumno = 0
# Tupla que almacenara las notas de cada alumno
notas = ()
# Diccionario que almacenara a cada alumno con sus notas
alumnos_notas = {}
# Variables para calcular el promedio de los alumnos
suma = 0
promedio = 0
# Lista paralela que almacenara el promedio de cada alumno
lista_promedio = []
# Variable que permite mostrar el promedio correspondiente a cada alumno
alumno_promedio = -1

# Bucle para que ingrese tres alumnos
for alumno in range(3):
    nombre_alumno = validar_nombre(alumnos_notas)
# Bucle para ingresar las 3 notas y para calcular la suma de las notas
    for nota in range (3):
        nota_alumno = entero_positivo()
        suma += nota_alumno
        notas.append(nota_alumno)
# Se almacena en el diccionario como clave el nombre del alumno y como valorla tupla de notas
# Se clcula el promedio
    promedio = suma / 3
    alumnos_notas[nombre_alumno] = notas

# Se muestra las notas de cada alumno y su promedio
for clave, valor in alumnos_notas.items():
    alumno_promedio += 1
    print(f"{clave}: {valor}")
    print(f"Promedio: {alumno_promedio}")


#================================================================================================================


#EJERCICIO 7
# Variables que almacenaran los alumnos que aprobaron los parciales
parcial_1 = {"1", "2", "3"}
parcial_2 = ("4", "3", "2", "5")
# Variable que Mostrara los aprobados en ambos parciales
aprobados_ambos = ""
# Variable que muestra todos los que aprobaron el primer parcial
aprobados_parcial_1 = ""
# Variable que muestra los que aprobaron los parciales
aprobados = ""

print("EJERCICIO 7")
aprobados_parcial_1 = parcial_1.difference(parcial_2)
aprobados_ambos = parcial_1. union(parcial_2)
aprobados = parcial_1.intersection(parcial_2)

# Muestra los aprobados del parcial 1
print("Aprobados del parcial 1:")
for aprobado in parcial_1:
    print(f"* {aprobado}")

# Muestra los todos los aprobados
print("Aprobados en ambos parciales:")
for aprobado in aprobados:
    print(f"* {aprobado}")

# Muestra a los quie aprobaron ambos parciales
print("Aprobados en general:")
for aprobado in aprobados_ambos:
    print(f"* {aprobado}")


#================================================================================================================


# EJERCICIO 8
# Diccionario de productos con su stock
stock_productos = {"Banana":5, "Huevos":6, "Caramelos":8}
# Variable para que el usuario ingrese la oción deseada
opcion = 0
# Variable para que el usuario busque o agregue un nuevo producto
producto = ""

print("EJERCICIO 8")
while True:
    # Se Muestra un menú para que el usuario elija si quiere agregar un producto, averiguar su stock o modificarlo
    print("                     Menú")
    print("1) Agregar un producto")
    print("2) Averiguar stock de un producto")
    print("3) Modificar stocl de un producto")
    print("4) Salir")
    print("Elija la opción deseada:")
    opcion = entero_positivo()
    print()


    if opcion == "1":
    # Bucle para validar que el usuario no deje el campo vacio y no ingrese un productoque ya forma parte del diccionario
        while True:
            producto =  validar_producto()
            if not producto in stock_productos:
                break
            else:
                print("Error, el producto que intentas ingresar ya se encuentra en el stock \n")

        print(f"Ingrese el stock del producto {producto}")
        stock_productos[producto] = entero_positivo()
        print()

    elif opcion == "2":
        # Se le pide al usuario que ingrese el nombre del producto que esta buscando
        print("Ingrese el nombre de ujn producto para er su stock:")
        producto = validar_producto()

    # Verifica que el producto se enncuentre en el stock en caso de ser asi se le mostrara cuantas unidades hay disponibles 
    # del producto, en caso de que el producto no se encuentre en el stock se le avisara al usuario de que el producto que 
    # buscaba no se encuentra en el stock
        if producto in stock_productos:
            print(f"El producto {producto} posee {stock_productos[producto]} unidades")
            print()
        else:
            print(f"El producto {producto}, no se encuentra en el stock")
            print()

    elif opcion == "3":
        while True:
    # Se le pide al usuario que ingrese el nombre del producto al cual quiere modificar su stock
            print("Ingrese un el nombre del producto del cual quiere modificar su stock:")
            producto = validar_producto()

    # Se fija si el producto se encuentra en el stock si es asi se modifica el stock si no le dice al usuari que 
    # ese producto no se encuentra en el stock y le vuelve a pedir que ingrese el producto
            if producto in stock_productos:
                print(f"Ingrese las unidades disponibles de {producto}")
                stock_productos[producto] = entero_positivo()
                break
            else:
                print("Error, el producto ingresado no se encuentra en el stock \n")

    elif opcion == "4":
        break

    else:
        print("Error, debes ingresar un número entre 1 y 4")


#================================================================================================================


# EJERCICIO 9
# Variable que almacena el día y horariode un evento específico 
agenda = {("Lunes", "8:00"): "Programación", ("Lunes","10:30"): "Arquitectura", ("Miércoles", "8:30"): "Matemática"}
# Variable para que el usuario consulte por un día
dia = ""
# Variable para que el usuario consulte por una hora y minuto específico
hora_minutos= ""
# Variable para buscar el valor en el diccionario
clave = ()

# Se le pide al usuario que ingrese el dia y hora para indicarl si hay o no un evento
print("EJERCICIO 9")
print("Ingrese un día y horario para saber si hay algún evento registrado")
dia = validar_dia()
print("El horario se mostrara en el siguiente formato 08:00, primero debes ingresar la hora y luego los minutos")
hora_minutos = validar_hora_minutos()
clave = (dia, hora_minutos)

# Se fija si hay algún evento en el día y horario ingresado, en caso de no t ener ningún evento se le comunica al usuario
# Si hay alún evento le mostrara cuál es
if not clave in agenda:
    print(f"El {dia}, a las {hora_minutos} no se tienenes ningún evento")
else:
    print(f"El {dia}, a las {hora_minutos} está programado el siguiente evento: {agenda[clave]}")
print()

#================================================================================================================


#EJERCICIO 10

# Diccionario que almacena países con sus capitales
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
# Variable que almacenara las capitales
capitales = ""
# Variable que almacenara los aíses
paises = ""
# Variable que almacenara el diccionario con lascapitales como clave y los paises como valor
inversa = {}

print("EJERCICIO 10")

# Bucle para invertir el ordden de los pares clave valor
for clave, valor in original.items():
    capitales = valor
    paises = clave
    inversa[capitales] = paises

# Muestra la lista origiinal
print("Lista Original: ")
for clave, valor in original.items():
    print(f"- {clave}: {valor}")
print()

# Muestra la lista Invertida
print("Lista al revez: ")
for clave, valor in inversa.items():
    print(f"- {clave}: {valor}")
print()