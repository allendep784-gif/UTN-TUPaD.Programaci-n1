from fact_numero import factorial_numero
from validaciones import validar_numero
from serie_fibo  import calcular_fibonacci
from calcular_potencia import potencia
from convertir_binario import decimal_a_binario
from var_palidermo import es_palindromo
from plabra_sin_tilde import obtener_palabra
from calculo_digitos import suma_digitos
from contador_bloques import contar_bloques
from contador_digitos import contar_digito

#====================================================================================================================
#Ejercicio 3

print("Cálculo de potencia")

print("Ingresá la base")
base = validar_numero()

print("Ingresá el exponente")
exponente = validar_numero()

resultado = potencia(base, exponente)
print()

print(f"{base} elevado a la {exponente} es: {resultado} \n")

#====================================================================================================================
#Ejercicio 4

print("Ingresá un número entero positivo para convertir a binario")
numero = validar_numero()
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")
print()

#====================================================================================================================
# Ejercicio 5

print("Verificador de palíndromos")

print("Ingresá una palabra sin espacios ni tildes")
palabra = obtener_palabra()

if es_palindromo(palabra):
    print(f"La palabra '{palabra}' ES un palíndromo.")
else:
    print(f"La palabra '{palabra}' NO es un palíndromo.")

#====================================================================================================================
#Ejercicio 6

print("Suma recursiva de dígitos")
print("Ingresá un número entero positivo para calcular la suma de todos sus dígitos.")
numero = validar_numero()

resultado = suma_digitos(numero)

print(f"\nLa suma de los dígitos del número {numero} es: {resultado}")
print()

#====================================================================================================================
#Ejercicio 7

print("Pirámide de bloques")
print("Este programa calcula cuántos bloques se necesitan para construir una pirámide.")
print("En el nivel más bajo hay n bloques, y cada nivel tiene uno menos que el anterior.")

# Pedir el número de bloques del nivel más bajo
print("\nIngresá la cantidad de bloques del nivel más bajo:")
n = validar_numero()

total = contar_bloques(n)

print(f"\nPara construir una pirámide con {n} bloques en el nivel más bajo,")
print(f"se necesitan un total de {total} bloques.\n")

#====================================================================================================================
# Ejercicio 8

print("=== CONTADOR DE DÍGITOS ===")
print("Este programa cuenta cuántas veces aparece un dígito dentro de un número.\n")

# Pedir número
print("Ingresá un número entero positivo")
numero = validar_numero()

# Pedir dígito

print("Ingresá el dígito que querés contar (0 a 9)")
while True:
    digito = validar_numero()
    if digito < 0 or digito > 9:
        print("Error: Debes ingresar un número entre 0 y 9.\n")
        continue
    break

# Llamar a la función
resultado = contar_digito(numero, digito)

# Mostrar resultado
print(f"\nEl dígito {digito} aparece {resultado} veces en el número {numero}.")