def sumaDigitosEnteroCorteMenos1():
    pares = 0
    while True:
        numero = int(input("Ingrese un número entero positivo (-1 para finalizar): "))
        if numero == -1:
            break
        suma_digitos = 0
        temp = numero
        while temp > 0:
            suma_digitos += temp % 10
            temp //= 10
        if suma_digitos % 2 == 0:
            pares += 1
        print(f"La suma de los dígitos de {numero} es {suma_digitos}")
    print(f"Se ingresaron {pares} números con suma de dígitos par.")

sumaDigitosEnteroCorteMenos1()