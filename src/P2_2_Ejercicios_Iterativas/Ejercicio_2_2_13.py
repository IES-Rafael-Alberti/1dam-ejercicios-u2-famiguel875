def ingresarSalir():
    while True:
        entrada = input("Ingrese algo (o 'salir' para terminar): ")
        if entrada.lower() == "salir":
            break
        print(entrada)

ingresarSalir()