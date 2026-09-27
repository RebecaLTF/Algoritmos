idades = []
alturas = []
for i in range(30):
    print(f"Aluno {i+1}:")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    idades.append(idade)
    alturas.append(altura)
media_altura = sum(alturas) / len(alturas)
media_inferior = 0
for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        media_inferior += 1
print("Média das alturas:", media_altura)
print("Quantidade de alunos com mais de 13 anos e altura inferior à média:", media_inferior)