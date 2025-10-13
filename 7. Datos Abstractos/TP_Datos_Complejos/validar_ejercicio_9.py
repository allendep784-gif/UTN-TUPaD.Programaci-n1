# Función que valida que el número ingres sea un entero positivo
def entero_positivo_9():
# Bucle que se repetira hasta que el usuario ingrese un número válido en caso de no ingresar el número válido
# se le informara la usuario de su error
    while True:
        try:
            numero = input()
            print()
            if not numero.isdigit():
                raise ValueError
            else:
                return numero
        except ValueError:
            print("Error, el valor ingresado no puede contener: ")
            print("- Coma")
            print("- Letras")
            print("- Números negativos")
            print("- Caracteres Especiales")
            print("- Tampoco puede quedar vacio")
            print()


#=======================================================================================================================


# Función para validar que se ingrese correctamente las horas y minutos
def validar_hora_minutos():

# Variables que almacenaran las horas y minutos
    hora = ""
    minutos = ""
# Variable que  almacenara la hora con los minutos
    hora_minutos = ""


# Bucle que se repetira hasta que se ingresen correctamente las horas y minutos
    while True:
        try:
            print("Ingrese la hora:")
            hora = entero_positivo_9()
            print("Ingrese los minutos:")
            minutos = entero_positivo_9()
            hora_completa = "" # Variablo de retorno
            longitud = 0 # Variable que almacenara los dígitos de hora y minutos
            numero = 0 # Numero almacenara el valor de hora o minutos transformados en int 


# Longitud almacenara cuántos dígitos tiene la hora
            longitud = len(hora)
# Condicional para validar que el formato de la hora se haya ingresado correctamente
# En caso de que hay dos dígitos se fija que no este por encima del valor máximo que puede tomar la hora que es 23
# Al ingresar la hora se valida que no ingrese un número negativo por eso solo nos fijamos que no se pase del valor máximo
            match longitud:
                case 2:
# Pasamos el str con la hora a int para verificar que no sea mayor a 23
                    numero = int(hora)
                    if numero > 23:
                        raise Exception
                case 1:
# En caso de que haya ingresado un dígito no hay que validar nada ya que solo pudo haber ingresado un número ente 0 y 9
# pero vamos agregarle un 0 delante para que se vea con el formato deseado
                    hora = "0" + hora
                case _ :
                    raise Exception


# Longitud almacenara cuántos dígitos tiene los minutos
            longitud = len(minutos)
            match longitud:
                case 1:
# En caso de que haya ingresado un dígito no hay que validar nada ya que solo pudo haber ingresado un número ente 0 y 9
# pero vamos agregarle un 0 delante para que se vea con el formato deseado
                    minutos = "0" + minutos
                case 2:
# Pasamos el str con la hora a int para verificar que no sea mayor a 59
                    numero = int(minutos)
                    if numero > 59:
                        raise Exception
                case _ :
                    raise Exception


# Se arma la hora con el formato correcto
            hora_completa = hora +  ":" + minutos
            return hora_completa



        except Exception:
            print(" EL valor ingresado no puede sr mayor a 23 en caso de la hora")
            print(" El valor ingresado no puede ser mayor a 59 en caso de los minutos")