lista_A = []
i = 0
while i < 10:
  números = int(input('Digite um número: '))
  lista_A.append(números)
  i += 1
soma = 0
for x in lista_A:
  soma += x ** 2
print(soma)