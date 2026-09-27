# QUESTÃO 45

altura = float(input('Altura: '))
if altura < 0:
  print('Altura inválida')
else:
  sexo = input('Selecione o sexo(f/m): ')
  if sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O peso ideal é: {peso_ideal}')
  elif sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f'O peso ideal é: {peso_ideal}')
  else:
    print('Sexo inválido')