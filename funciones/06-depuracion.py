def largo(texto):
    result = 0
    for _ in texto:
        result += 1
    return result


l = largo("Hola mundo")
print(l)
