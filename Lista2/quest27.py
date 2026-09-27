# QUESTÃO 27

p1 = float(input('Informe o preço do bolo: '))
p2 = float(input('Informe o preço dos salgados: '))
p3 = float(input('Informe o preço dos docinhos: '))
if p1 < p2 and p1 < p3:
  print('Você deve comprar o bolo')
elif p2 < p3:
  print('Você deve comprar os salgados')
else:
  print('Você deve comprar os docinhos')