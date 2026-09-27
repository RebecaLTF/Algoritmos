# QUESTÃO 07

idades = []
alturas = []
for i in range(1, 11):
  idade = int(input('Digite uma idade: '))
  altura = float(input('Digite uma altura: '))
  idades.append(idade)
  alturas.append(altura)
alturas_copy = alturas.copy()
alturas_copy.sort()
maior_altura = alturas.index(alturas_copy[-1])
print(f"A pessoa de maior altura: {alturas[maior_altura]}, tem {idades[maior_altura]} anos")