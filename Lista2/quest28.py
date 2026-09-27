# QUESTÃO 28

turno = input('Turno que você estuda: ')
if turno == 'M' or turno == 'Maturino':
  print('Bom Dia!')
elif turno == 'V' or turno == 'Vespertino':
  print('Boa Tarde!')
elif turno == 'N' or turno == 'Noturno':
  print('Boa Noite!')
else:
  print('Valor Inválido!')