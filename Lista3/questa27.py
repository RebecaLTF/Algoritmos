# QUESTÃO 27
i = 0
while i < 3:
  login = input('Digite o login: ')
  senha = input('Digite a senha: ')
  if login == 'kezia' and senha == '123':
    print('Acesso permitido')
    i += 3
  else:
    print('Login e/ou senha inválidos. Tente novamente')
    i += 1