# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor sejá inválido e continue pedindo até que o usuário informe um valor válido.
# While é usado quando vai haver repetição com uma quantidade desconhecida de termos.
# Fazer esse programa em uma página sozinho. Vai entrar em loop.

nota = int(input('Digite um valor: '))
while nota < 0 or nota > 10:
  print('Nota inválida')
  nota = float(input('Digite um valor: '))