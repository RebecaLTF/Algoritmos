# QUESTÃO 03

lista = []
for i in range(1, 41):
  notas = float(input('Digite uma nota: '))
  lista.append(notas)
  média = sum(lista) / len(lista)
print(lista)
print(f'A média das notas é: {média}')