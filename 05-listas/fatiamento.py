lista = [2,3,4,5,6]
print(lista[0:2])

lista = [2,3,4,5,6]
print(lista[2:4])
print(lista[:3])
print(lista[1:])
print(lista[:])

lista = [2,3,4,5,6]
print(lista[-2:])

lista = [2,3,4,5,6]
print(lista[-2:-4]) #erro. resultado= []
print(lista[-4:-2])

lista = [2,3,4,5,6]
lista[1] = 1
print(lista)