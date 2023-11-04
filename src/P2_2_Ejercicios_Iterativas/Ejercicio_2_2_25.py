def analizaFrases():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    palabra_mas_larga = max(palabras, key=len)
    cantidad_palabras = len(palabras)
    print(f"La palabra más larga es '{palabra_mas_larga}' y hay {cantidad_palabras} palabras en total.")

analizaFrases()