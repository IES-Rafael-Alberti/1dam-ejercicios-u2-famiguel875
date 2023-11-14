def menu123():
    notas = []

    while True:
        print("MENÚ")
        print("----")
        print("1 - Introduzca una nota")
        print("2 - Imprimir listado")
        print("3 - Finalizar programa")
    
        opcion = input("Seleccione una opción => ")

        if opcion == "1":
            nota = float(input("Introduzca una nota: "))
            notas.append(nota)
            print(f"Nota {nota} añadida correctamente.")
        elif opcion == "2":
            if len(notas) == 0:
                print("No se han ingresado notas aún.")
            else:
                print("Listado de notas:")
                for i, nota in enumerate(notas, start=1):
                    print(f"Nota {i}: {nota}")
        elif opcion == "3":
            print("Finalizando programa.")
            break
        else:
            print("Opción incorrecta. Por favor, elija una opción válida.")

menu123()