# Faça um programa que peça a idade e a altura de 10 pessoas, armazene cada informação na sua respectiva lista. Imprima a idade da pessoa que possui maior altura.

idades = []
alturas = []
for i in range(10):
  idade = int(input('Idade:'))
  idades.append(idade)
  altura = float(input('Altura:'))
  alturas.append(altura)
maior = max(alturas)
indiceMaior = alturas.index(maior)
idadeMaior = idades[indiceMaior]
print(idadeMaior)