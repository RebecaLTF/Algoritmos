# QUESTÃO 01

print('Média de 30 alunos')
for i in range(1, 31):
  nota1 = float(input('Digite a 1ª nota: '))
  nota2 = float(input('Digite a 2ª nota: '))
  média = (nota1 + nota2) / 2
  if média >= 7:
    print(f'O aluno {i} foi aprovado com média {média}')
  else:
    print(f'O aluno {i} foi reprovado com média {média}')