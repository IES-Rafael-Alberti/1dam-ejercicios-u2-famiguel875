def sumaDigitosEntero():
    numero = int(input("Ingrese un número entero positivo: "))
    suma_digitos = 0
    while numero > 0:
        suma_digitos += numero % 10
        numero //= 10
    print("La suma de los dígitos es:", suma_digitos)

sumaDigitosEntero()