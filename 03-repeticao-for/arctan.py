# Faça um programa que recebe o número real x como entrada e devolva uma aproximação do arco tangente de x (em radianos) através da série:
# a) arctan(x) = x - (x**3/3) + (x**5/5) - (x**7/7) + ...
# b) Considere a aproximação para 50 termos.
# exp = 1
# for i in range(50):
#          monta o termo
#          exp += 2


expoente = 1
sinal = 1
arctan = 0

x = float(input('Digite um número: '))
for i in range(50):
  arctan += sinal * ((x**expoente)/expoente)
  expoente += 2 # expoente = expoente + 2
  sinal *= -1 # sinal = sinal * (-1)
print(arctan)