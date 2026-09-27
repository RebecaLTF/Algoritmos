l = [0.7,-1.4,122,90,-65]
 # l= [-4,-44,-9,-1]
maior = l[0]
 # for i in range(1,len(l)):
 #     if l[i] > maior:
 #         maior = l[i]
 # print(maior)


for numero in l:
  if numero > maior:
    maior = numero
print(maior)

print(max(l))