def division(num1, num2):
    if num2 == 0:
        return print("ERROR")
    else:
        return print(num1 / num2)

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

division(num1, num2)