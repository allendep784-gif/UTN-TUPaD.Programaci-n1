def obtener_palabra():
    while True:
        palabra = input("Ingresá una palabra sin espacios ni tildes: ").lower()

        # Verificar que no tenga espacios
        if " " in palabra:
            print("Error: la palabra no debe contener espacios.")
            continue

        # Verificar que solo tenga letras
        if not palabra.isalpha():
            print("Error: solo se permiten letras (sin números ni símbolos).")
            continue

        # Verificar que no tenga tildes (á, é, í, ó, ú)
        tildes = "áéíóú"
        if any(letra in palabra for letra in tildes):
            print("Error: la palabra no debe contener tildes.")
            continue

        return palabra
