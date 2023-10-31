lista1 = []
lista2 = []
for i in range(1, 6):
    lista1.append(int(input(f"Digite o {i}º elem. 1a. lista: ")))
for i in range(1, 6):
    lista2.append(int(input(f"Digite o {i}º elem. 2a. lista: ")))

conjunto_uniao = set(lista1).union(set(lista2))

print(f"Conjunto da união entre as duas listas:")
print(conjunto_uniao)
