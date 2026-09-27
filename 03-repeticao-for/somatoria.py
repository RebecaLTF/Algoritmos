# Faça um programa para ler um valor x e calcular Y=1X+2X+3X+4X+...+20X.
x = float(input())
y = 0
for i in range(1,21):
  y = y + (i) * x #y += i*x
print(y)