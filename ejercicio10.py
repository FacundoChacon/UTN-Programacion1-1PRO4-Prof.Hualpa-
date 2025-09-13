n =  input("Ingrese el numero de patente que quiera buscar: ").upper()
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
encontrado = False
for i in range(0, 26):
    for j in range(0, 26):
        for k in range(0, 26):
            for x in range(0, 10):
                for y in range(0, 10):
                    for z in range(0, 10):
                        patente = letras[i] + letras[j] + letras[k] + str(x) + str(y) + str(z)
                        if patente == n:
                            print("Patente encontrada")
                            print("La patente es: ", patente)
                            encontrado = True
                            break
                    if encontrado:
                        break
                if encontrado:
                    break
            if encontrado:
                break
        if encontrado:
            break
    if encontrado:
        break
if not encontrado:
    print("Patente no encontrada")