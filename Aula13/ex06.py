def converte(x,y,z):
    minuto = (x * 3600) + (y * 60) + z
    return minuto

v1 = int(input("Digite a hora: "))
v2 = int(input("Digite os minutos: "))
v3 = int(input("Digite os segundos: "))
valor = converte(v1, v2, v3)

print(f"{v1}h, {v2}min e {v3}s correspondem à {valor} segundos")
