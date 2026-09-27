lista = ["a","b","c","d","e","f"]
lista[1:3]+[]
print(lista)

lista = ["a", "d", "f"]
lista[1:1] = ["b", "c"]  # Insere "b" e "c" na posição 1
print(lista)  # O resultado será ['a', 'b', 'c', 'd', 'f']
