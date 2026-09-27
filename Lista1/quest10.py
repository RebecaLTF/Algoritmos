# QUESTÃO 10 - Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

dólar = float(input('A cotação atual do dólar é: '))
valor = float(input('A quantidade de dinheiro que o usuário tem disponível em dólar para conversão é: '))
x = valor/dólar
print('O usuário tem', x,'reais')