d = {}

for _ in range(5):
    nome = input("Digite seu nome: ")
    idade = int(input("Entre com sua idade: "))
    d[nome] = idade

idades = list(d.values())
media_idade = sum(idades) / len(idades)
print(f'A média das idades é {media_idade}')

for chave, valor in d.items():
    if valor > media_idade:
        print(f'Nome: {chave}')
