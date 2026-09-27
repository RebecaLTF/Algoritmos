# QUESTÃO 11 - Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a.m.

depósito = float(input('Valor depositado: '))
jurosam = 0.7/100
rendimento = depósito*(1+jurosam)**1
print('O rendimento após um mês é de', rendimento,'reais')