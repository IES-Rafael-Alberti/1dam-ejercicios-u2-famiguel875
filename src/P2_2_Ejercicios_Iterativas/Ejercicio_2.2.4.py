def cuentaAtras(numero):
    cuenta_atras = [str(i) for i in range(numero, -1, -1)]
    resultado = ", ".join(cuenta_atras)
    print(resultado)

numero = int(input("Ingrese un número entero positivo: "))

cuentaAtras(numero)