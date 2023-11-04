def sumatorio():
    total = 0
    while True:
        numero = int(input("Ingrese un número (0 para finalizar): "))
        if numero == 0:
            break
        total += numero
    print("La sumatoria de los números ingresados es:", total)

sumatorio()