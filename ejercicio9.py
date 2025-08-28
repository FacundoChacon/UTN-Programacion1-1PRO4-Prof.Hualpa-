INTERES_MENSUAL = 0.02
MESES = 12

monto = float(input("Ingrese el monto solicitado: "))

monto_total = monto * (1 + INTERES_MENSUAL) ** MESES
cuota_mensual = monto_total / MESES

print(f"Monto total a devolver: ${monto_total}")
print(f"Valor de cada cuota mensual: ${cuota_mensual}")