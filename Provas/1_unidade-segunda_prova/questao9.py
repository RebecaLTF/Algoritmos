notas = []
valor = 0.0
while valor != -1:
    valor = float(input("Digite uma nota: "))
    if valor != -1:
      notas.append(valor)

# a)
quantidade = len(notas)
print(f"Quantidade de valores lidos: {quantidade}")

# b)
print("Valores na ordem original:")
print(notas)

# c)
print("Valores na ordem inversa:")
print(list(reversed(notas)))

# d)
soma = sum(notas)
print(f"Soma dos valores: {soma}")

# e)
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0
print(f"Média dos valores: {media}")

# f)
acima_media = sum(1 for n in notas if n > media)
print(f"Quantidade de valores acima da média: {acima_media}")

# g)
abaixo_de_sete = sum(1 for n in notas if n < 7)
print(f"Quantidade de valores abaixo de sete: {abaixo_de_sete}")

# h)
print("Programa encerrado.")