# SE IMOPORTA LA UNA FUNCIÓN PARA PODER ELEGIR UNA PALABRA AL AZAR
import random
# IMPORTAMOS FUNCIÓN QUE DARA LA BIENVENIDA Y MOSTRARA LAS REGLAS
from bienvenida_reglas import *
# SE IMPORTA FUNCIÓN PARA VALIDAR LA PALABRA INGRESADA POR ELL USUARIO
from validaciones import *
# SE IMPORTA FUNCIÓN mostrar la palabra
from mostrar_palabra import *


#=============================================================================================================================
# DEFINICIÓN DE VARIABLES

# VARIABLE QUE ALMACENA LAS PALABRAS QUE EL JUGADOR PODRA ADIVINAR
palabras = ["FUSELAJE", "AVIÓN", "MOTOR", "CABINA", "RADAR", "FLAPS" ]
# VARIABLE QUE ALMACENARA LA PALABRA A ADIVINAR
palabra_adivinar = random.choice(palabras)
# VARIABLE QUE ALMACENARA LA LETRA QUE INTENTA ADIVINAR EL USUARIO
letra_elegida = ""
# VARIABLE QUE ALMACENA LOS INTENTOS DEL USUARIO
intentos = 5
# VARIABLE QUE ALMACENA LOS INTENTOS QUE HA UTILIZADO
intentos_utilizados = 0
# MATRIZ PARA MOSTRAR EL TÍPICO MUÑECO DEL JUEGO
munieco =[
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
# VARIABLE BANDERA PARA SABER SI EL USUARIO ADIVINO LA PALABRA
adivino = False


#=============================================================================================================================
# ALGORITMO PRINCIPAL
# SE LE DA LA BIENVENIDA AL USUARIO Y SE LE EXPLICA LAS REGLAS
bienvenida_reglas()

# BUCLE QUE SE REPETIRA HASTA QUE EL USUARIO ADIVINE LA PALABRA O SE QUEDE SIN INTENTOS
# A CADA ITERACIÓN DEL BUCLE LE RESTAMOS UN INTENTO AL USUARIO QUE SERA EL QUE ESTA 
# USANDO EN ESE MOMENTO Y SE LE INCREMENTARA 1 INTENTO EN INTENTOS UTILIZADOS PARA
# PODER LLEVAR UN CONTEO DE LOS INTENTOS UTILIZADOS.
while intentos > 0 and adivino == False:
    intentos -= 1
    intentos_utilizados += 1


# SE LLAMA A UNA FUNCIÓN PARA VALIDAR QUE INGRESE UN VALOR ESPERADO.
    letra_elegida = validar_letra_palabra()


# FUNCIÓN QUE MOSTRA PARTES DE LA PALABRA A ADIVINAR
    mostrar_palabra(palabra_adivinar)

# EN CASO DE LA LONGITUD DE letra_elegida SEA 1 QUIERE DECIR QUE INGRESO UNA LETRA CASO
# CONTRARIO INGRESO UNA PALABRA.
# SI EL USUARIO INGRESO DIRECTAMENTE LA PALABRA SE FIJARA SI ADIVINO O NO, EN CASO DE ADIVINAR GANARA
# SI NO PERDERA,
    if len(letra_elegida) > 1:
        if letra_elegida == palabra_adivinar:
            adivino = True
            break
        else:
            adivino = False
            break


if not adivino:
    munieco =[
    [None, "O", None],
    ["-", "|", "-"],
    ["¡", None, "¡"]
]

