nombre = "Pablo"
cadena = "Buenos días mundo!!"

nombre2 = "Andrés"
apellido = "Allende"
nombre_completo = (f"{nombre2} {apellido}")

nombre_mayuscula = "PABLO ALLENDE"
nombre_minuscula = nombre_mayuscula.lower()

solo_primer_letra_mayuscula =nombre_mayuscula.capitalize()

numero1 = 8
numero2 = 20.14
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

precio = 1700.50
descuento = 0.9
precio_final = 17000.50 - (17000 * 10 / 100)

edad = 19 + 5 - 10

altura = 1.75 * 4 / 3

longitud = len(cadena)

precio = int(15000.14)

print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} X {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division}")