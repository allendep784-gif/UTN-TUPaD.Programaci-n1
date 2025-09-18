print("Ejercicio For \n")
alfabeto = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
alfabeto = alfabeto.split(",")
print(alfabeto)
mensaje_a_encriptar = input("Ingrese los 5 mensajes a encriptar separados por una coma: ")
mensaje_a_encriptar = mensaje_a_encriptar.upper().split(",")
corrimiento = int(input("Ingrese cuantas letras desea desplazarce para encriptar el mensaje: "))
proceso_encriptacion = ""
mensaje_encriptado = []
posicion = 0
letra = ""

# Bucle para encriptar todas las palabras ingresadas
for mensaje in mensaje_a_encriptar:
    # Obtenemos la posición de cada caracter que se almacena en la variable mensaje
    for indice in range(0, len(mensaje)):
        # Se fija si el caracter está en el alfabeto
        if mensaje[indice] in alfabeto:
            # Se asigna el caracter a la variable letra para buscarla en la variable alfabeto
            letra = mensaje[indice]
            # Busca en que posicion se encuentra la letra
            posicion = alfabeto.index(letra)
            # Se encripta la letra
            letra = alfabeto[posicion + corrimiento]
            # Se empieza a encriptar el mensaje
            proceso_encriptacion = proceso_encriptacion + letra
        else:
            # En caso de que el caracter no sea una letra se lo asignamos a al mensaje
            proceso_encriptacion = proceso_encriptacion + mensaje[indice]
    
    mensaje_encriptado.append(proceso_encriptacion)

for n in range(0, len(mensaje_encriptado)):
    print(f"Mensaje {n + 1}, {mensaje_encriptado[n]}")

print("\n")

print("Ejercicio While \n")
import random
PIEDRA = 1
PAPEL = 2
TIJERA = 3
eleccion_jugador = 1
eleccion_maquina = 0
ganadas_jugador = 0
ganadas_computadora = 0

print("             PIEDRA, PAPEL O TIJERA \n")
while eleccion_jugador != 0:
    print("1)_ Piedra")
    print("2)_ Papel")
    print("3)_ Tijera")
    print("0)_ Salir")
    eleccion_jugador = int(input("Elija la jugada deseada: "))
    eleccion_maquina = random.randint(1, 3)
    if eleccion_jugador == 3 and eleccion_maquina == 2:
        ganadas_jugador += 1
        print(f"La PC elijio: {eleccion_maquina}")
        print("Gana el jugador\n") 
    elif eleccion_jugador == 1 and eleccion_maquina == 3:
        ganadas_jugador += 1
        print(f"La PC elijio: {eleccion_maquina}")
        print("Gana el jugador\n") 
    elif eleccion_jugador == 2 and eleccion_maquina == 1:
        ganadas_jugador += 1
        print(f"La PC elijio: {eleccion_maquina}")
        print("Gana el jugador\n") 
    elif eleccion_jugador == 3 and eleccion_maquina == 1:
        ganadas_computadora += 1
        print(f"La PC elijio: {eleccion_maquina}")
        print("Gana la PC\n") 
    elif eleccion_jugador == 2 and eleccion_maquina == 3:
        ganadas_computadora += 1
        print(f"La PC elijio: {eleccion_maquina}")
        print("Gana la PC\n")
    elif eleccion_jugador == 1 and eleccion_maquina == 2:
        ganadas_computadora += 1
        print(f"La PC elijio: {eleccion_maquina}")
        print("Gana la PC\n") 
    elif eleccion_jugador == 3 and eleccion_maquina == 3 or eleccion_jugador == 1 and eleccion_maquina == 1 or eleccion_jugador == 2 and eleccion_maquina == 2:
        print("Fue un empate")
