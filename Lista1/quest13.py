# QUESTÃO 13 - Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

custo = float(input('O preço de custo do brigadeiro é de '))
percentual = float(input('O percentual é de '))
venda = custo+(percentual)
print('O brigadeiro será vendido por', venda,'reais')