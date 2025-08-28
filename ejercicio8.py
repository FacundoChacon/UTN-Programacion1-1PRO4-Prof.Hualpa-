
CONSUMO_LITROS_100KM = 8
VELOCIDAD_PROMEDIO = 90

distancia = float(input("Ingrese la distancia a recorrer en km: "))
precio_litro = float(input("Ingrese el precio de la gasolina por litro: "))

litros_necesarios = (distancia / 100) * CONSUMO_LITROS_100KM
costo_viaje = litros_necesarios * precio_litro
tiempo_horas = distancia / VELOCIDAD_PROMEDIO

print(f"Litros necesarios: {litros_necesarios}")
print(f"Costo del viaje: ${costo_viaje}")
print(f"Tiempo estimado de viaje: {tiempo_horas} horas")