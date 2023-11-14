def mayoriaEdad(edad):
    if edad >= 18:
        return print("Es mayor de edad")
    else:
        return print("Es menor de edad")

edad = int(input("Introduzca su edad "))

mayoriaEdad(edad)