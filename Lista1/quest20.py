# QUESTÃO 20 - Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

a = input('A: ')
b = input('B: ')
a, b = b, a
print('A:', a)
print('B:', b)