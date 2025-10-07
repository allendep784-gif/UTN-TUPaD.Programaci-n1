# FUNCIÓN QUE VÁLIDA QUE EL USUARIO HAYA INGRESADO UNA LETRA O PALABRA
def validar_letra_palabra():

# ESTE BUCLE SE REPETIRA HASTA QUE EL USUARIO INGRESE UN VALOR VÁLIDO
    while True:

# SE LE PIDE AL USUARIO INGRESAR UN NÚMERO Y SE ESTANDARIZA PARA HACER LA VALIDACIÓN
# LE QUITAMOS LOS ESPACIOS CON .STRIP() PARTA VALIDAR SI DEJO O NO A LA VARIABLE VACIA
# .UPPER SE UTILIZA PARA PODER COMPARAR CORRECTAMENTE LAS LETRAS
        letra = input("Ingrese la letra o palabra: ").strip().upper()


# SI EL USUARIO NO INGRESO NADA SE LE INFORMA SOBRE EL ERROR Y SE LE VUELVE A PEDIR QUE INGRESE UNA LETRA
        if letra == "":
            print("Error, no puedes dejar este espacio vacío \n")
            continue


# EN CASO DE QUE EL VALOR INGRESADO TENGA UNA LONGITUD DE 1 QUIERE DECIR QUE INGRESO UNA LETRA SI TIENE MÁS ES UNA PALABRA
# SI INGRESA SOLO UN CARACTER SE FIJA SI ES UNA LETRA EN CASO DE NO SER UNA LETRA LE INFORMARA AL USUARIO Y LE VOLVERA A 
# PEDIR QUE INGRESE UNA LETRA, AHORA BIEN, SI INGRESO UNA PALABRA SE VA A RECORRER CON UN BUCLE FOR CARACTER POR CARACTER
# EN CASO DE QUE ENCUENTRE UN CARACTER DISTINTO A UNA LETRA LE INFORMARA AL JUGADOR DEL ERROR Y LE PEDIRA NUEVAMENTE QUE 
# INGRESE UNA LETRA O PALABRA
        if len(letra) == 1:
            if letra >= "A" and letra <= "Z":
                return letra
            else:
                    print("Error, debes ingresar una letra del alfabeto \n")
                    continue
        else:
            for caracter in range(len(letra)):
                if letra[caracter] >= "A" and letra[caracter] <= "Z":
                    pass
                else:
                    print("Error, debes ingresar una letra del alfabeto \n")
                    continue
                return letra


print(validar_letra_palabra())