# QUESTÃO 03

n = int(input('Digite um número: '))
if n < 0:
  print('Não é possível calcular o fatorial de um número negativo')
else:
  fatorial = 1
  for i in range(1, n + 1):
    fatorial = fatorial * i
  print(f'O fatorial de {n} é {fatorial}')