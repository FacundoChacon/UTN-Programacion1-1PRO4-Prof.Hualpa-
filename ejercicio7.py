TASA_COP = 4000
TASA_ARS = 850
TASA_EUR = 0.92

usd = float(input("Ingrese el monto en dólares (USD): "))

cop = usd * TASA_COP
ars = usd * TASA_ARS
eur = usd * TASA_EUR

print(f"{usd} USD equivalen a:")
print(f"{cop} Pesos Colombianos")
print(f"{ars} Pesos Argentinos")
print(f"{eur} Euros")