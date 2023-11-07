from math import pi
def volume(n):
    calculo = (4 * pi * (n ** 3)) / 3
    return calculo

r = float(input("Digite o raio: "))
valor = volume(r)
print(f"O volume da esfera é{valor: .2f}m³")


