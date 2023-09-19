ValorDaCompra = float(input("Digite o valor da compra: "))

if ValorDaCompra <= 1000.00:
    desconto = ValorDaCompra - (ValorDaCompra * 0.10)
    print(f"O desconto é de 10% e o valor final do produto será de {desconto:.2f}")
elif ValorDaCompra > 1000.00:
    desconto_2 = ValorDaCompra - (ValorDaCompra * 0.20)
    print(f"desconto é de 20% e o valor final do produto será de {desconto_2:.2f}")
elif ValorDaCompra > 5000.00:
    desconto_3 = ValorDaCompra - (ValorDaCompra * 0.30)
    print(f"desconto é de 30% e o valor final do produto será de {desconto_3:.2f}")

