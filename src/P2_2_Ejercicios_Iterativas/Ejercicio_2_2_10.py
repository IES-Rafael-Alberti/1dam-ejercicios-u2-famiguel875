def esPrimo(numero):
    es_primo = True
    if numero < 2:
        es_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

numero = int(input("Ingrese un número entero: "))

esPrimo(numero)