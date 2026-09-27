# QUESTÃO 02

num = float(input('Digite o 1º número: '))
maior = num
menor = num
for i in range(2,11):
  num = float(input(f'Digite o {i}º número: '))
  if num > maior:
    maior = num
  if num < menor:
    menor = num
print(f'Maior número digitado:{maior}')
print(f'Menor número digitado:{menor}')