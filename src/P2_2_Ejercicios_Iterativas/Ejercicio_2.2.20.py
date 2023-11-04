def buscaletra():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    posicion = -1
    for i, caracter in enumerate(frase):
        if caracter == letra:
            posicion = i
            break
    if posicion != -1:
        print(f"La letra '{letra}' se encontró en la posición {posicion}.")
    else:
        print(f"La letra '{letra}' no se encontró en la frase.")

buscaletra()