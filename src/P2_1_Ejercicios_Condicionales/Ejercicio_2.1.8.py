def rendimiento(puntuacion):
    if puntuacion == 0.0:
        return print(f"Su nivel de rendimiento es: Inaceptable y la cantidad de dinero que recibirá es: {0} €") 
    elif puntuacion == 0.4:
        return print(f"Su nivel de rendimiento es: Aceptable y la cantidad de dinero que recibirá es: {2400} €") 
    elif puntuacion >= 0.6:
        return print(f"Su nivel de rendimiento es: Meritorio y la cantidad de dinero que recibirá es: {puntuacion * 2400} €") 
    else:
        return print("Valor de puntuación erróneo")

puntuacion = float(input("Ingrese su puntuación: "))

rendimiento(puntuacion)