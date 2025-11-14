def validar_numero():
    while True:
        try:
            numero = input("Esperando número: ").strip()

            if not numero:
                print("Error: Este campo no puede quedar vacío. \n")
                continue
            
            if not numero.isdigit() or numero == "0":
                raise ValueError
            else:
                numero = int(numero)
                return numero
        
        except ValueError:
            print("Error: El valor ingresado no puede contener: ")
            print("- Letras")
            print("- Espacios")
            print("- Caracteres especiales")
            print("- Números negativos")
            print("- Ser igual a cero \n")

if __name__ == "__main__":
    numero = validar_numero()