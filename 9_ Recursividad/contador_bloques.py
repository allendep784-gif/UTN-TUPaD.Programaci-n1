def contar_bloques(n):
    # Caso base: la cima de la pirámide
    if n == 1:
        return 1
    
    # Parte recursiva: n + contar_bloques(n-1)
    return n + contar_bloques(n - 1)
