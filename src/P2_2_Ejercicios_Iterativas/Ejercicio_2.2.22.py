def contarDigitosParesImpares():
    digitos_pares = 0
    digitos_impares = 0
    while True:
        numero = int(input("Ingrese un número entero positivo (0 para finalizar): "))
        if numero == 0:
            break
        while numero > 0:
            digito = numero % 10
            if digito % 2 == 0:
                digitos_pares += 1
            else:
                digitos_impares += 1
            numero //= 10
    print(f"Total de dígitos pares: {digitos_pares}")
    print(f"Total de dígitos impares: {digitos_impares}")

contarDigitosParesImpares()