# QUESTÃO 30

valor_da_hora = float(input('Valor da hora: '))
horas_trabalhadas = int(input('Horas trabalhadas: '))
salário_bruto = valor_da_hora * horas_trabalhadas
inss = salário_bruto * 0.1
fgts = salário_bruto * 0.11
if salário_bruto <= 900.00:
  ir = 0
else:
  if salário_bruto > 900.00 and salário_bruto <= 1500.00:
    ir = salário_bruto * 0.05
  else:
    if salário_bruto > 1500.00 and salário_bruto <= 2500.00:
      ir = salário_bruto * 0.1
    else:
      if salário_bruto > 2500.00:
        ir = salário_bruto * 0.2
print(f'Salário Bruto: {salário_bruto}')
print(f'IR: {ir}')
print(f'INSS: {inss}')
print(f'FGTS: {fgts}')
print(f'Total de descontos: {ir + inss}')
print(f'Salário Líquido: {salário_bruto - ir - inss}')