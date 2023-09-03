# Interactive
# Hay numero "Ingrese un numero"
# Ingrese operation
# Ingrese otro num
# resultado
# guardar result como firt num

num1 = 0
num = 0
oper = ""

num1 = int(input("Ingrese un numero: "))

while oper.lower() != "salir":
    print("Operando con s r d m salir")
    oper = input("Ingrese una operacion: ")
    if oper.lower() != "salir":
        num = int(input("Ingrese otro numero: "))

    if oper.lower() == "s":
        num1 += num
    elif oper.lower() == "r":
        num1 -= num
    elif oper.lower() == "m":
        num1 *= num
    elif oper.lower() == "d":
        num1 /= num
    print("--------------------------------")
    print(f"El resultado es {num1}")
    print("--------------------------------")
