palavra = input("Entre com a palavra: ")

palavraigual = palavra[::-1].lower()

if palavra.lower() == palavraigual.lower():
    print(f"A {palavra} é um palídromo")
else:
    print(f"A {palavra} não é um palídromo")
