def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numeros_primos = 0
while True:
    numero = int(input("Ingrese un número mayor que 1 (0 para finalizar): "))
    if numero == 0:
        break
    if es_primo(numero):
        numeros_primos += 1

print(f"Se ingresaron {numeros_primos} números primos.")