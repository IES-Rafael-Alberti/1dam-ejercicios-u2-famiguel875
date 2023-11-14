def grupoAoB(nombre, sexo):
    if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
        return print("Usted pertenece al grupo: A")
    else:
        return print("Usted pertenece al grupo: B")

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ")

grupoAoB(nombre, sexo)