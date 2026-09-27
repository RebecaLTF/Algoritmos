# QUESTÃO 05

lista_médias = []
maiores = []
soma = 0
for i in range(1,11):
  notas = []
  for x in range(1,5):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    soma += nota
  média = soma / 4
  lista_médias.append(média)
  if média >= 7:
    maiores.append(média)
print(maiores)