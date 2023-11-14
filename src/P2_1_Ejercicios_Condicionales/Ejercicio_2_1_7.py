def tipoImpositivoRenta(renta_anual):
    if renta_anual < 10000:
        return print(f"Su tipo impositivo es de {0.05}") 
    elif renta_anual <= 20000:
        return print(f"Su tipo impositivo es de {0.15}") 
    elif renta_anual <= 35000:
        return print(f"Su tipo impositivo es de {0.20}") 
    elif renta_anual <= 60000:
        return print(f"Su tipo impositivo es de {0.30}") 
    else:
        return print(f"Su tipo impositivo es de {0.45}") 

renta_anual = float(input("Ingrese su renta anual en euros: "))

tipoImpositivoRenta(renta_anual)