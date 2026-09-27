cotacao = float(input('Cotação: '))
valorDolares = float(input('Valor em dólares: '))
valorReais = valorDolares * cotacao
print('Valor em reais:', valorReais)
print('')

deposito = float(input('Valor depositado: '))
acrescimo = deposito * 0.7/100
rendimento = deposito + acrescimo
print(rendimento)
print('')

entrada=input('Nome: ')
print('O nome informado foi:', entrada)
print('O nome informado foi: '+ entrada)