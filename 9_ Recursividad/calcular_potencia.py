def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    else:
        # Caso recursivo: n^m = n * n^(m-1)
        return base * potencia(base, exponente - 1)
