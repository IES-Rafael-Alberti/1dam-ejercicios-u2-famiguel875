def comprobarContrasenia(contrasenia_correcta):
    while True:
        contrasenia = input("Ingrese la contraseña: ")
        if contrasenia == contrasenia_correcta:
            print("Contraseña correcta. Acceso permitido.")
            break
        else:
            print("Contraseña incorrecta. Inténtelo de nuevo.")

contrasenia_correcta = "contrasenia"

comprobarContrasenia(contrasenia_correcta)