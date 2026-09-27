contMas = contFem = 0
for i in range(10):
  pessoas = input('Informar apenas f ou m: ')
if pessoas == 'f':
  contFem = contFem + 1
elif pessoas == 'm':
  contMas += 1
else:
  print('Sexo inválido')
print(contFem, contMas)