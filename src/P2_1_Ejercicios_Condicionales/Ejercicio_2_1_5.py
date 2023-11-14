def tributar(edad, ingresos):
    if edad > 16 and ingresos >= 1000:
        return print("Tienes que tributar")
    else:
        return print("No tienes que tributar")

edad = int(input("¿Cuál es tu edad? "))
ingresos = int(input("¿Cuáles son tus ingresos mensuales? "))

tributar(edad, ingresos)