def pizzaVegetariana(opcion):
    if opcion.lower() == "sí" or "si":
        ingredienteAdicional = int(input("¿Quiere un ingrediente adicional? (Presione el número indicadado si lo desea) \n1 -> pimiento\n2 -> tofu\n"))
        if ingredienteAdicional == 1:
            ingredientes = ["mozzarella", "tomate", "pimiento"]
            ingredientesString = ", ".join(ingredientes)
            return print(f"Su pizza es vegetariana y sus ingredientes son: {ingredientesString}")
        elif ingredienteAdicional == 2:
            ingredientes = ["mozzarella", "tomate", "tofu"]
            ingredientesString = ", ".join(ingredientes)
            return print(f"Su pizza es vegetariana y sus ingredientes son: {ingredientesString}")
        else:
            ingredientes = ["mozzarella", "tomate"]
            ingredientesString = ", ".join(ingredientes)
            return print(f"Su pizza es vegetariana y sus ingredientes son: {ingredientesString}")
    else:
        ingredienteAdicional = int(input("¿Quiere un ingrediente adicional? (Presione el número indicadado si lo desea) \n1 -> peperoni\n2 -> jamón\n 3 -> salmón\n"))
        if ingredienteAdicional == 1:
            ingredientes = ["mozzarella", "tomate", "peperoni"]
            ingredientesString = ", ".join(ingredientes)
            return print(f"Su pizza no es vegetariana y sus ingredientes son: {ingredientesString}")
        elif ingredienteAdicional == 2:
            ingredientes = ["mozzarella", "tomate", "jamón"]
            ingredientesString = ", ".join(ingredientes)
            return print(f"Su pizza no es vegetariana y sus ingredientes son: {ingredientesString}")
        elif ingredienteAdicional == 3:
            ingredientes = ["mozzarella", "tomate", "salmón"]
            ingredientesString = ", ".join(ingredientes)
            return print(f"Su pizza no es vegetariana y sus ingredientes son: {ingredientesString}")
        else:
            ingredientes = ["mozzarella", "tomate"]
            ingredientesString = ", ".join(ingredientes)
            return print(f"Su pizza no es vegetariana y sus ingredientes son: {ingredientesString}")

opcion = input("¿Quiere una pizza vegetariana? (Sí/No): ")

pizzaVegetariana(opcion)