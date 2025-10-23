# Importa funciones creadas por el desarrollador
from Funciones_TP import *


#======================================================================================================================================


# ALGORITMO PRINCIPAL
# DFINICIÓN VARIABLES
# Variable para agregar un producto al archivo
linea_agregar = ""
# Variable que alamacenara las lineas del archivo como lista
productos =[]
# Variable para buscar un producto
buscar_producto = ""
# Variable para saber si se encuentra el producto que se esta buscando
esta = False


#======================================================================================================================================


print("Ejercicio 1")
print("Generando archivos")
print()
# Archivo que almacenara distintos productos
with open("productos.txt", "w") as archivo:
    archivo.write("Nombre,Precio,Cantidad\n")
    archivo.write("Play Station 5,800000,15\n")
    archivo.write("Xbox Series X,800000,15\n")
    archivo.write("Nintendo Switch 2,700000,9\n")


#======================================================================================================================================


print("Ejercicio 2")
# Muestra los elementos del archivo
mostrar_productos("productos.txt")


#======================================================================================================================================


# Se agrega una nueva linea al archivo
print("Ejercicio 3")
linea_agregar = agregar_productos("productos.txt")
with open("productos.txt", "a") as archivo:
    archivo.write(linea_agregar)

# Muestra los elementos del archivo
mostrar_productos("productos.txt")


#======================================================================================================================================


print("Ejercicio 4")
# Carga los datos del archivo en una lista de diccionario
productos = cargar_productos("productos.txt")

print("Mostrando lista con los productos del archivo")
for producto in productos:
    print(f"{producto["Nombre"]} | {producto["Precio"]} | {producto["Cantidad"]}")
print()


#======================================================================================================================================


print("Ejercicio 5")
buscar_producto = input("Ingrese el nombre del producto que esta buscando: ").strip().title()

for diccionario in productos:
    if diccionario["Nombre"] == buscar_producto:
        esta = True
        # Muestra la información del producto al usuario
        print()
        print(f"Información del producto {buscar_producto}:")
        for clave, valor in diccionario.items():
            if clave == "Precio":
                print(f"{clave}: ${valor}")
            else:
                print(f"{clave}: {valor}")
        break
# Si no se encontro el producto se le informa al usuario
if not esta:
    print(f"Error, el producto {buscar_producto} no se encuentra en la lista.")
print()


#======================================================================================================================================


print("Ejercicio 6")
# Llama a una funcion que se encarga de sobrescribir el archivo
sobrescribir_archivo("productos.txt", productos)

# Muestra los elementos del archivo
with open("productos.txt", "r") as contenido:
# Variable que almacenara todos los productos para procesarlos.
        lineas = contenido.readlines()
# Variable que mostrara los productos con su precio y cantidad.
        informacion_producto = []

# Muestra los elementos del archivo
print("Encabezado: Nombre | Precio | Cantidad")
mostrar_productos("productos.txt")