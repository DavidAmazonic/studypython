numeros = list(range(20))


# FEO
# first = numeros[0]

# second = numeros[1]

# third = numeros[2]

first, *otros, last = numeros

print(first, otros, last)

first, second, *otros = numeros

print(first, second, otros)
