def lectorDeTitulos():
    lineas_completas = 0
    sumatorio_total_digitos = 0

    while True:
        titulo = input("Libro: ")
        if titulo == "*":
            break
    
        if titulo == "/":
            print(f"Línea completa. Aparecen {sumatorio_total_digitos} dígitos numéricos.")
            sumatorio_total_digitos = 0
            lineas_completas += 1
        else:
            total_digitos = sum(1 for letra in titulo if letra.isdigit())
            sumatorio_total_digitos += total_digitos

    print(f"Fin. Se leyeron {lineas_completas} líneas completas.")

lectorDeTitulos()