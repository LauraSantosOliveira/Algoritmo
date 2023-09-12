X = float(input("Entre com o número x: "))
Y = float(input("Entre com o número y: "))
Z = float(input("Entre com o número z: "))
if (X + Y > Z) and (X + Z > Y) and (Y + Z > X):
    # é um triangulo
    if X == Y == Z:
        print("É um triângulo Equilátero")
    elif (X == Y) or (X == Z) or (Y == Z):
        print("É um triângulo Isósceles")
    else:
        print("É um triângulo Escaleno")

else:
    # não é um triângulo
    print("Os lados não formam um triângulo!!")
