# QUESTÃO 17 - Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

i1 = int(input('Escolha um número inteiro: '))
i2 = int(input('Escolha outro número inteiro: '))
r3 = float(input('Escolha um número real: '))

# o produto do dobro do primeiro com metade do segundo.
x = (2*i1)+(i2/2)

# a soma do triplo do primeiro com o terceiro.
y = (3*i1)+r3

# o terceiro elevado ao cubo.
z = r3**3

print(x, y, z)