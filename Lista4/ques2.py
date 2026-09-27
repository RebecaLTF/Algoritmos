# QUESTÃO 02

lista = []
for i in range(1, 11):
  números = float(input('Digite um número: '))
  lista.append(números)
cópia = lista.copy()
cópia.reverse()
print(cópia)