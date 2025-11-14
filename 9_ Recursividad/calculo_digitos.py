def suma_digitos(n):
    # Caso base: si n es un solo dígito
    if n < 10:
        return n
    
    # Caso recursivo:
    # Último dígito: n % 10
    # Resto del número: n // 10
    return (n % 10) + suma_digitos(n // 10)
