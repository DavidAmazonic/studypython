mascotas = ["wolf", "pelusa", "copito", "Alfa"]
print(mascotas[0])
mascotas[0] = "Perla"
# print(mascotas)
# print(mascotas[2:])
# print(mascotas[-1])
# print(mascotas[1:2:2])  # print de saltos de a dos

mascotas.remove("pelusa")
print(mascotas)

numeros = list(range(21))
print(numeros[::2])  # numer par
print(numeros[1::2])  # numer inpar
print(numeros[1:10:2])  # Ultimo numvber
