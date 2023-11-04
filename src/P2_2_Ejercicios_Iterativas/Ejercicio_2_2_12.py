def letraFrase(frase, letra):
    contador = frase.count(letra)
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

letraFrase(frase, letra)