def ehprimo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

valor = int(input("Digite um número: "))
if ehprimo(valor):
    print(f"O número {valor} é primo")
else:
    print(f"O número {valor }não é primo")