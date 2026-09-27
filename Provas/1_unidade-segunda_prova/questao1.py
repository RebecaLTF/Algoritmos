números = []
i = 0
while i < 50:
  número = int(input('Digite um número inteiro: '))
  números.append(número)
  i += 1
soma = 0
multiplicação = 1
for x in números:
  soma += x
  multiplicação *= x
print(soma)
print(multiplicação)
print(números)