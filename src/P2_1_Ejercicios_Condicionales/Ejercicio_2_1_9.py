def precio(edad):
    if edad < 4:
        return print("La entrada es gratis")
    elif 4 <= edad <= 18:
        return print("El precio de la entrada es 5 euros")
    else:
        return print("El precio de la entrada es 10 euros")

edad = int(input("Ingrese la edad del cliente: "))

precio(edad)