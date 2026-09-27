# QUESTÃO 09

lista1 = []
lista2 = []
lista3 = []
for i in range(1, 11):
  num1 = float(input('Digite um número: '))
  lista1.append(num1)
  lista3.append(num1)
  num2 = float(input('Digite um número: '))
  lista2.append(num2)
  lista3.append(num2)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")