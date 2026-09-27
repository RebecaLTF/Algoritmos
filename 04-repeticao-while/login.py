# Faça um programa para validar o login e a senha de um usuário. Caso o usuário informe algum valor inválido informar o erro e pedir novamente os dados. A leitura dos
# dados deve ser encerrada quando o usuário digitar 3 vezes um valor inválido (login ou senha). Considere o login válido como \"kezia\" e a senha como \"123\".
nome = input()
senha = input()
cont = 1
while cont<3 and (nome != 'kezia' or senha != "123"):
  print('Login ou senha inválidos! Tente novamente.')
  nome = input('Nome: ')
  senha = input('Senha: ')
  cont += 1
if nome == 'kezia' and senha == "123":
  print('Login válido.')
else:
  print('Esgotou possibilidades.')