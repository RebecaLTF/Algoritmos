nomes = []
for i in range(10):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    nomes.append(nome)
procura = input("Digite um nome para procurar: ")
if procura in nomes:
    print("ACHEI")
else:
    print("NÃO ACHEI")