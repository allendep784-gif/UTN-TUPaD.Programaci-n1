def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Si la primera y la última letra no coinciden → no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    
    # Llamada recursiva con la palabra sin primera y última letra
    else:
        return es_palindromo(palabra[1:-1])
