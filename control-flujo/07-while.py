# numero = 1
# cal = True
# while cal == True:
#     print(numero)
#     numero *= 2
#     if numero > 1000:
#         cal = False
comando = ""

while True:
    comando = input('$ ')
    print(comando)
    if comando.lower() == 'salir':
        break
