# Función que mostrara los productos del archivo.
def mostrar_productos(archivo):

# Se abre el archivo para trabajar con el
    with open(archivo, "r") as contenido:
# Variable que almacenara todos los productos para procesarlos.
        productos = contenido.readlines()
# Variable que mostrara los productos con su precio y cantidad.
        informacion_producto = []

# Recorre linea por lenea sin contar el encabezado para mostrar los productos.
# Se utiliza .strip() y .split(",") para borrar los espaciosy generar una lista.
        for linea in range(len(productos)):
            if not linea == 0:
                informacion_producto = productos[linea].strip().split(",")
                print(f"Producto: {informacion_producto[0]} | Precio: {informacion_producto[1]} | Cantidad: {informacion_producto[2]}")
        print()


# =====================================================================================================================================


# Funcion para agregar productos al arcivo
def agregar_productos(archivo):
# Se define tres variables para almacenar el nombre del producto su precio y cantidad.
    nombre_producto = ""
    precio = ""
    cantidad = ""
# Variable que almacenara la información del producto
    linea_agregar = ""
# Variables para verificar que no ingresen un producto ya ingresado
    partes = []
    nombre_ya_ingresado = True


# Se abre el archivo con permisos para agregarle contenido sin eliminar el contenido que traía.
    with open(archivo, "r") as contenido:

# LISTA QUE ALMACENARA LAS LINEAS DEL ARCHIVO
        productos = contenido.readlines()

# BUCLE QUE SE REPETIRA HASTA QUE EL USUARIO INGRESE EL NOMBRE DE UN PRODUCTO
        while nombre_ya_ingresado == True:
            nombre_producto = input("Ingrese el nombre del producto: ").strip().title()

# VERIFICA QUE EL USUARIO NO DEJE EL CAMPO VACÍO
            if nombre_producto == "":
                print("Error, no puedes dejar este campo vacío")
                continue

# BUCLE QUE RECORRE LOS ELEMENTOS DE LA LISTA PRODUCTOS (SON STRINGS), ESTOS ELEMENTOS SE CONVERTIRAN MOMENTANEAMENTE EN LISTAS,
# DE ESTA MANERA SE PODRA ACCEDER A CADA ELEMENTO DE LA "SUB_LISTA" PARA PODER VEIFICAR QUE EL USUARIO NO HAYA INGRESADO EL NOMBRE 
# DE UN PRODUCTO YA EXIXTENTE
            for linea in range(len(productos)):
                partes = productos[linea].strip().split(",")
                if nombre_producto in partes:
                    print(f"Error, el producto {partes[0]} ya fue ingresado")
                    print()
                    nombre_ya_ingresado = True
                    break
                else:
                    nombre_ya_ingresado = False


        print()
# Se le pide al usuario que ingrese el precio del producto y la cantidad del producto
        print("Ingrese el precio del producto")
        precio = validar_precio()
        print("Ingrese las unidades disponibles del producto")
        cantidad = entero_positivo()

# Se genera la linea a agregar
    linea_agregar = nombre_producto + "," + precio + "," + cantidad + "\n"
    return linea_agregar


#======================================================================================================================================


# Función para validar que el usuario haya ingresado el precio correcto
def validar_precio():
    numero = ""
    # Variable para verificar que el numero ingresado sea un número float
    numero_flotante = 0
    while True:
        try:
            numero_flotante = float(input("Esperando número positivo: "))
            print()
            if numero_flotante == 0 or numero_flotante <= 0:
                raise ValueError
            else:
                numero = str(numero_flotante)
                return numero
        except ValueError:
            print("Error, el valor ingresado no puede contener: ")
            print("- Letras")
            print("- Números negativos")
            print("- Caracteres Especiales")
            print("- No puede ser igual a cero")
            print("- Tampoco puede quedar vacio")
            print()

#======================================================================================================================================


# Función que valida que el número ingres sea un entero positivo
def entero_positivo():
# Bucle que se repetira hasta que el usuario ingrese un número válido en caso de no ingresar el número válido
# se le informara la usuario de su error
    while True:
        try:
            numero = input("Esperando número positivo:")
            print()
            if not numero.isdigit() or numero == "0":
                raise ValueError
            else:
                return numero
        except ValueError:
            print("Error, el valor ingresado no puede contener: ")
            print("- Coma")
            print("- Letras")
            print("- Números negativos")
            print("- Caracteres Especiales")
            print("- No puede ser igual a cero")
            print("- Tampoco puede quedar vacio")
            print()


#======================================================================================================================================


#Función para agregar los elementos del archivo a la lista de diccionarios
def cargar_productos(archivo):
    # Variable que almacena el contenido del archivo
    productos = []
    # Variable que almacena cada linea como una lista
    partes_lineas =[]
    # Variable a retornar
    lista_diccionario = []

    # Leo archivo y registro sus lineas
    with open(archivo, "r") as conenido:
        productos = conenido.readlines()

    # Bucle que recorre las lineas del archivo omitiendo el encabezado
    for linea in productos[1:]:
        partes_lineas = linea.strip().split(",")
        # Diccionario que almacena la información del producto
        info_producto = {'Nombre': partes_lineas[0], 'Precio': partes_lineas[1], 'Cantidad': partes_lineas[2]}
        lista_diccionario.append(info_producto)

    return lista_diccionario


# Función para sobrescribir el archivo
def sobrescribir_archivo(archivo, lista):
    with open(archivo, "w") as contenido:
        # Genera el encabezado del archivo
        contenido.write("Nombre,Precio,Cantidad \n")
        # Recorre cada diccionario para agregar sus valores a la nueva linea del archivo
        for producto in lista:
            # Se genera una variable que sera utilizada para agregar una nueva linea al archivo
            linea = producto["Nombre"] + "," + producto["Precio"] + "," + producto["Cantidad"] + "\n"
            contenido.write(linea)