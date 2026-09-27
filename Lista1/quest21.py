# QUESTÃO 21 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

ganha = float(input('Quanto você ganha por hora: '))
horas = int(input('Número de horas que você trabalhou no mês '))

# salário bruto.
sb = ganha*horas

# quanto pagou ao INSS.
inss = sb*0.08

# quanto pagou ao sindicato.
sindicato = sb*0.05

# calcule os descontos e o salário líquido, conforme a tabela abaixo:
   # Salário Bruto : R$
print('Seu Salário Bruto é de', sb)

   # IR (11%) : R$
ir = sb*0.11
print('O IR corresponde a', ir)

   # INSS (8%) : R$
print('O INSS corresponde a', inss)

   # Sindicato(5%) : R$
print('O Sindicato corresponde a', sindicato)

   #TOTAL DE DESCONTOS : R$
td = ir + inss + sindicato
print('O total de descontos corresponde a:', td)

   # Salário Líquido : R$
sl = sb-(td)
print('Seu Salário Líquido é de', sl)
