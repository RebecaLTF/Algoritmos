# QUESTÃO 04

lista = []
lista_pares = []
lista_ímpares = []
for i in range(1, 21):
  números = int(input('Digite um número: '))
  lista.append(números)
  if números % 2 == 0:
    lista_pares.append(números)
  else:
    lista_ímpares.append(números)
print(lista)
print(lista_pares)
print(lista_ímpares)