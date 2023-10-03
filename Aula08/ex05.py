palavra = input("Entre com a palavra: ")
frase = input("Entre com a frase: ")

qtd = frase.count(palavra)
total_palavras = frase.count(' ') + 1

print(f'A frase possui um total de {total_palavras} palavras!')
print(f"A palavra {palavra} foi encontrada {qtd} vezes na frase")
