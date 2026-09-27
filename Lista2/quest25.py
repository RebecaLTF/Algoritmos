# QUESTÃO 25

nota1 = float(input('Sua nota 01 é: '))
nota2 = float(input('Sua nota 02 é: '))
med = (nota1+nota2)/2
if med == 10:
  print('Aprovado(a) com Distinção')
elif med >= 7:
  print('Aprovado(a)')
else:
  print('Reprovado(a)')