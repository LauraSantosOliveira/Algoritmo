comprimento = float(input("Entre com o comprimento: "))
altura = float(input("Entre com a altura: "))
porta = 1.68
pintura = (comprimento * altura) * 4 - porta

print(f"A àrea total que será pintada é de {pintura}")
print(f"Será necessário {pintura / 3:.2f} litros de tinta para pintar as paredes")
print(f"Será necessário {round(pintura / 18)} latas de tinta para pintar as paredes")
print(f"Será necessário {round(pintura / 3.6)} galões de tinta para pintar as paredes")
