def soma_digitos(numero):
    total = sum(int(digito) for digito in numero if digito.isdigit())
    return total

def multiplicar_digitos(numero):
    resultado = 1
    for digito in numero:
        if digito.isdigit():
            resultado *= int(digito)
    return resultado

    total = (int(digito) for digito in numero if digito.isdigit())
    return total

num = input("Digite um número em formato de string: ")
if num.isdigit():
    numero = int(num)
    resultado = soma_digitos(num)
    resultado2 = multiplicar_digitos(num)
    print(f"A soma dos dígitos do número {numero} é: {resultado}")
    print(f"A multiplicação dos dígitos do número {numero} é {resultado2}")
else:
    print("Entrada inválida. Certifique-se de inserir apenas caracteres numéricos.")
