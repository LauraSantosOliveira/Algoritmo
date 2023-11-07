from funcoes import ehprimo

def qtd_primos(p):
    qtd = 0
    for i in range(1, p+1):
        if ehprimo(i):
            qtd = qtd + 1
    return qtd

valor = int(input("Entre com o número: "))
print(f"A quantidade de primos entre 1 e {valor} é: ")
print(f"{qtd_primos(valor)}")
