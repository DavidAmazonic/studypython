def suma(*numbers):
    resultado = 0
    for number in numbers:
        resultado += number
    print(resultado)


suma(2, 5)
suma(3, 5, 7, 24)
suma(4, 5, 42)
