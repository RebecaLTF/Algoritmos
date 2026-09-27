x = float(input('a: '))
if x == 0:
  print('Programa encerrado')
else:
  y = float(input('b: '))
  z = float(input('c: '))
  delta = (y**2)-(4*x*z)
  if delta < 0:
    print('A equação não possui raízes reais')
  elif delta == 0:
    raiz = -y/(2*x)
    print('A equação possui apenas uma raíz real:', raiz)
  else:
    x1 = (-y + (delta **(1/2))) / (2*x)
    x2 = (-y + (delta **(1/2))) / (2*x)
    print('A equação possui duas raízes reais:', x1, x2)