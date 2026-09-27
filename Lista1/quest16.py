# QUESTÃO 16 - Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e o salário no final do mês.

nome = input('Nome do vendedor(a): ')
salário = float(input('Salário fixo: '))
vendas = float(input('Total de vendas efetuadas no mês: '))
variável = (vendas * 0.15)
x = salário + variável
print(nome, salário, x)