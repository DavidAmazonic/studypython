animal = '  calaMardo felizardo  '

# Metodo MAYUSCULAS

print(animal.upper())

# metodo minusculas

print(animal.lower())

# metodo Titulo Todo

print(animal.title())

# meto borra espacios <- y ->   (rstrip() y lsrtrip()

print(animal.strip())

# metodo Pirmera mayuscual

print(animal.strip().capitalize())

# metodo EN contrar parte dentro del string

print(animal.find('Ma'))

# metodo remplazar

print(animal.replace('Mar', 'ja'))

# metodo saber si se encuentra Boleano

print('Mar' in animal)
print('Mar' not in animal)