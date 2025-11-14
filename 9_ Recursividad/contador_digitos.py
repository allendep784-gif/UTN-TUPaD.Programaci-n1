def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    
    # Tomo el último dígito
    ultimo = numero % 10
    
    # Si el último dígito coincide, contamos 1, si no, contamos 0
    coincidencia = 1 if ultimo == digito else 0
    
    # Llamada recursiva con el número sin el último dígito
    return coincidencia + contar_digito(numero // 10, digito)