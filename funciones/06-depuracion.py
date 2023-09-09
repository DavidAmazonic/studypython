def largo(texto):
    result = 0
    for char in texto:
        result += 1
    return result


l = largo("Hola mundo")
print(l)
