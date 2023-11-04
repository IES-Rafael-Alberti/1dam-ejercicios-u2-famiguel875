def capitalInversion(cantidad, interes, anios):
    for i in range(anios):
        cantidad *= 1 + interes / 100
        print(f"Año {i + 1}: {cantidad:.2f}€")

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interés anual en porcentaje: "))
anios = int(input("Ingrese el número de años: "))

capitalInversion(cantidad, interes, anios)