"""
edad = int(input("Introduzca su edad "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
"""
"""
def importeconIVA(importesinIVA, tipoIVA):
    total = importesinIVA + (importesinIVA * tipoIVA/100)
    print(f"El precio final del artículo es de {total} €")

importesinIVA = float(input("Importe sin IVA de un artículo: "))
tipoIVA = float(input("Tipo de IVA a aplicar en %: "))

# Llama a la función para ejecutarla
importeconIVA(importesinIVA, tipoIVA)
"""

def mayoriaEdad(edad):
    if edad >= 18:
        return print("Es mayor de edad")
    else:
        return print("Es menor de edad")

edad = int(input("Introduzca su edad "))

mayoriaEdad(edad)