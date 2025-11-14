def decimal_a_binario(n):
    # Caso base: cuando n es 0 o 1, lo devolvemos como cadena
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    
    # Parte recursiva:
    else:
        # n // 2 → siguiente número a convertir
        # n % 2 → resto (0 o 1)
        return decimal_a_binario(n // 2) + str(n % 2)
