#  Escrever um programa que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100].
# A entrada de dados deve terminar quando for lido um número negativo.

cont_0_25=cont_26_50=cont_51_75=cont_76_100=0
num = float(input('Digite um número: '))
while num >= 0:
  if num>=0 and num<=25:
    cont_0_25 +=1
  elif num>=26 and num<=50:
    cont_26_50 +=1
  elif num>=51 and num<=75:
    cont_51_75 +=1
  elif num>=76 and num<=100:
    cont_76_100 +=1
  num = float(input('Digite um número:' ))
print(cont_0_25, cont_26_50, cont_51_75, cont_76_100)