def montoCompra():
    total = 0
    while True:
        monto = float(input("Ingrese el monto de la compra (0 para finalizar): "))
        if monto == 0:
            break
        elif monto < 0:
            print("Monto negativo, no se procesa.")
        else:
            total += monto
    if total > 1000:
        total -= total * 0.10
    print(f"El total a pagar es: ${total:.2f}")
montoCompra()