lista1 = []
lista2 = []
lista3 = []
lista4 = []
for i in range(1, 11):
  num1 = float(input('Digite um número para a Lista 1: '))
  lista1.append(num1)
  lista4.append(num1)
  num2 = float(input('Digite um número para a Lista 2: '))
  lista2.append(num2)
  lista4.append(num2)
  num3 = float(input('Digite um número para a Lista 3: '))
  lista3.append(num3)
  lista4.append(num3)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")
print(f"Lista 4: {lista4}")