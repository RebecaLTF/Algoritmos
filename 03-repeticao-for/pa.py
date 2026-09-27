# Escreva um programa que imprima N termos de uma Progressão Aritmética, conforme a fórmula a seguir. O usuário deverá fornecer o valor de:
# n (número de termos), r (razão) e a1 (primeiro termo da série)
# a1 = a1
# a2 = a1 + r
# a3 = a2 + r
# a4 = a3 + r
# an = a1 + (n-1).r
# Se não colocar o 2 no range, a fórmula será aplicada no a1
# Se não colocar o +1 no após o n, no caso do n ser 3 a fórmula só será aplicada até o segundo termo.

a1 = float(input('Selecione o valor inicial: '))
r = float(input('Selecione a razão: '))
n = int(input('Selecione o número de termos: '))
print(a1)
for i in range(2,n + 1):
  an = a1 + (i - 1) * r
  print(an)