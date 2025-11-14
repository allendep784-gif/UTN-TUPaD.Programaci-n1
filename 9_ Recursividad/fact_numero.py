
def factorial_numero(num):
    return 1 if num == 1 else num * factorial_numero(num-1)

#====================================================================================================================

if __name__ == "__main__":
    print(factorial_numero(5))
