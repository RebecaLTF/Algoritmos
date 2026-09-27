l1 = [3, 2, 1, 3, 0, -5, 4, 3]
l2 = [4, 345, 0, -4, 2, 56, 3]
intersecao = []
i = 0
for elemento in l1:
  if (elemento in l2) and (elemento not in intersecao):
     intersecao[i:i] = [elemento]
     i+= 1
print(intersecao)