# Función que valida que el número ingres sea un entero positivo
def entero_positivo():
# Bucle que se repetira hasta que el usuario ingrese un número válido en caso de no ingresar el número válido
# se le informara la usuario de su error
    while True:
        try:
            numero = input("Ingrese un número: ")
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


#=========================================================================================================================


# Función que valida un si se ingresa un nombre ya existente y también valida que no se deje el campo vacío
def validar_nombre(diccionario):
# Variable que almacenara el nombre del contacto
    contacto = ""

    while True:
        contacto = input("Ingrese el nombre del contacto: ").strip().capitalize()

        if contacto == "":
            print("Error, no puedes dejar este campo vacío \n")
            continue
        elif contacto in diccionario:
                print("Error, este contacto ya existe \n")
                continue
        else:
            return contacto


#=========================================================================================================================


# Función para validar el nombre del producto
def validar_producto():
# Variable que almacenara el nombre del producto
    producto = ""

    while True:
        producto = input("Ingrese el nombre del producto: ").strip().capitalize()

        if producto == "":
            print("Error, no puedes dejar este campo vacío \n")
            continue
        else:
            return producto


#=========================================================================================================================


# Función para validar el nombre del producto
def validar_dia():
# Variable que almacenara el nombre del dia
    dia = ""

    while True:
        dia = input("Ingrese el día: ").strip().capitalize()

        if dia == "":
            print("Error, no puedes dejar este campo vacío \n")
            continue

        match dia:
            case "Lunes":
                return dia
            case "Martes":
                return dia
            case "Miércoles":
                return dia
            case "Jueves":
                return dia
            case "Viernes":
                return dia
            case "Sábado":
                return dia
            case "Domigo":
                return dia
            case _ :
                print(f"{dia} no es un dia de la semana")
                print()


#=========================================================================================================================


# Función para contar la cantidad de veces que se repite una palabra
def contador_palabra(palabra, lista):
# Variable para contar la cantidad de veces que aparece una palabra
    contador = 0
    for vocablo in lista:
        if palabra == vocablo:
            contador += 1

    return contador