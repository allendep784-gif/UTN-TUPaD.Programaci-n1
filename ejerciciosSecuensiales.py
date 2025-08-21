monto_total = float(input("Ingrese el monto total de la cuenta: "))
propina_10_porciento = monto_total * 10 / 100
propina_15_porciento = monto_total * 15 / 100

print()
print(f"Propina sugerida (10%): {propina_10_porciento}")
print(f"Total a pagar con la propina de 10%: {monto_total + propina_10_porciento}")
print()

print(f"Propina sugerida (15%): {propina_15_porciento}")
print(f"Total a pagar con la propina de 15%: {monto_total + propina_15_porciento}")