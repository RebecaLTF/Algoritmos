# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno, imprima o número de

medias = []
contNotasAcima7 = 0
for i in range(10): #10 alunos
   print("Notas para aluno", str(i+1))
   somaNota = 0 # essa variável está dentro do for pois precisa ser zerada sempre que o laço recomeça, caso contrário, se estivesse fora, a soma das notas estaria sempre reaproveitando o resto das notas do aluno anterior.
   for j in range(4):
    nota = int(input("Nota:"))
    somaNota += nota
   media = somaNota/4
   medias.append(media)
   if media >= 7:
    contNotasAcima7 += 1
print(medias)
print(contNotasAcima7)