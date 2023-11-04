def sumatorioEnteros():
    total = 0
    while True:
        numero = int(input("Ingrese un número (0 para finalizar): "))
        if numero == 0:
            break
        if numero > 0:
            total += numero
    print("La sumatoria de los números positivos ingresados es:", total)

sumatorioEnteros()