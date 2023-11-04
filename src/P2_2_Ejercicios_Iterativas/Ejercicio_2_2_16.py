def sumatorioMayor():
    mayor = 0
    while True:
        numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))
        if numero == 0:
            break
        if numero > mayor:
            mayor = numero
    print("El mayor número ingresado es:", mayor)

sumatorioMayor()