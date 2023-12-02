lista = []
def eh_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def qtd_primos(p):
    qtd = 0
    for i in range(1, p+1):
        if eh_primo(i):
            qtd += 1
    return qtd
def list_primos(i):
    mult = i * 2 + 5
    while i < mult:
        if eh_primo(i):
            lista.append(i)
        i += 1
    return tuple(lista)

def soma_primos(numero):
    total = sum(lista_primos)
    return total

num = int(input("Entre com um número: "))
if eh_primo(num):
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
quantidade_primos = qtd_primos(num)
print(f"A quantidade de primos entre 1 e {num} é: {quantidade_primos}")

lista_primos = list_primos(num)
print(f"Os números primos entre 1 e {num} são: {lista_primos}")

print(f"A soma dos números é: {soma_primos(num)}")








