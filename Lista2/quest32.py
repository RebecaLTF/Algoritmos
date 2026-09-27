# QUESTÃO 32

not1 = float(input('Digite a 1ª nota parcial: '))
not2 = float(input('Digite a 2ª nota parcial: '))
x = (not1 + not2) / 2
print(not1,not2,x)
if 9<=x==10:
  print('Conceito: A, APROVADO')
elif 7.5<=x<9:
  print('Conceito: B, APROVADO')
elif 6<=x<7.5:
  print('Conceito: C, APROVADO')
elif 4<=x<6:
  print('Conceito: D, REPROVADO')
elif 0<=x<4:
  print('Conceito: E, REPROVADO')
else:
  print('erro')