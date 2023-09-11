num = [2, 4, 135, 56, 7]

num.sort()  # sort reordena la lista
print(num)

num.sort(reverse=True)  # sort reordena la lista alreves
print(num)

numeros = sorted(num)   # sorted nueva lista ordenada
print(numeros)

numeros = sorted(num, reverse=True)   # sorted nueva lista ordenada
print(numeros)

usuarios = [[4, "Carl"], [1, "Felip"], [2, "Andre"], [3, "Ester"]]

usuarios.sort()
print(usuarios)

usuarios = [["Carl", 4], ["Felip", 5], ["Andre", 2], ["Ester", 2]]


def ordena(elenent):
    return elenent[1]


usuarios.sort(key=ordena)
print(usuarios)

usuarios.sort(key=ordena, reverse=True)
print(usuarios)
# ok
