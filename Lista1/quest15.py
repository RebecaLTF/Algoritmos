# QUESTÃO 15 -Escreva um programa que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão.

A = int(input('Prineiro número '))
B = int(input('Segundo número '))
C = int(input('Terceiro número '))
R = (A + B)**2
S = (B + C)**2
D = (R + S)/2
print('A expressão tem', D,'como resultado')