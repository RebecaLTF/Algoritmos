l1 = [3, 2, 1, 3, 0, -5, 4, 3]
l2 = [4, 345, 0, -4, 2, 56, 3]
uniao = []
for elemento in l1:
  if elemento not in uniao:
    uniao += [elemento]
for elemento in l2:
  if elemento not in uniao:
    uniao += [elemento]
print(uniao)