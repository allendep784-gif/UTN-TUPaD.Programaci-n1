
def calcular_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

#====================================================================================================================

if __name__ == "__main__":
    print(calcular_fibonacci(10))
