# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5

x = int(input('Digite um dos números que deseja multiplicar: '))
y = int(input('Digite outro dos números que deseja multiplicar: '))
if x<0 and y<0:
  print('Valor inválido')
else:
  z = x*y
print(x ,'X', y,'=', z)