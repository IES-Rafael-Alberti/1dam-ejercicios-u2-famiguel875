def aniosCumplidos(edad):
    for i in range(1, edad + 1):
        print("Ha cumplido", i, "años.")

edad = int(input("Ingrese su edad: "))

aniosCumplidos(edad)