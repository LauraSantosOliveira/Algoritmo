soma = 0
MediaIdade = int(input("Entre com a quantidade de idade que deseja fazer a média: "))
for i in range(1, MediaIdade+1):
    n = int(input(f"Entre com o {i}ª idade: "))
    soma = soma + n
media = soma / MediaIdade
print(f"A média das idades é {media:5.2f}")
