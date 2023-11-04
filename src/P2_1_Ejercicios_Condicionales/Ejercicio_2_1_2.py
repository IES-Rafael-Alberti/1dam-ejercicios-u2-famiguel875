def comprobarContraseña(password1, password2):
    if password1.upper() == password2.upper():
        return print("Contraseña correcta")
    else:
        return print("Contraseña errónea")
    
password1 = input("Introduzca la contraseña: ")
password2 = "contraseña"

comprobarContraseña(password1, password2)