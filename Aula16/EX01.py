def calcular_patoseCoelhos(total_cabecas, total_pes):
    total_cabecas_equacao = total_cabecas * 2 + 5
    total_pes_equacao = total_pes * 3 + 7

    total_patos = (total_pes_equacao - total_cabecas_equacao) // 2
    total_coelhos = total_cabecas - total_patos

    return total_patos, total_coelhos

total_cabecas = int(input("Digite o total de cabeças: "))
total_pes = int(input("Digite o total de pés: "))

resultados = calcular_patoseCoelhos(total_cabecas, total_pes)

print(f"Total de patos: {resultados[0]}")
print(f"Total de coelhos: {resultados[1]}")