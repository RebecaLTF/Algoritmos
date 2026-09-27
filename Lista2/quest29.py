# QUESTÃO 29

money = float(input('Salário atual: '))
if money <= 280.00:
  reajuste = money * 0.2
else:
  if money > 280.00 and money <= 700.00:
    reajuste = money * 0.15
  else:
    if money > 700.00 and money <= 1500.00:
      reajuste = money * 0.1
    else:
      reajuste = money * 0.05
print(f'Salário antes do reajuste: {money}')
print(f'Valor do reajuste: {reajuste}')
print(f'Novo salário: {money + reajuste}')