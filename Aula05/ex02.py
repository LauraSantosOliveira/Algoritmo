nota1 = float(input("Entre com a Nota 01: "))
nota2 = float(input("Entre com a Nota 02: "))
nota3 = float(input("Entre com a Nota 03: "))
media = (nota1 + nota2 + nota3) / 3

if media < 3:
    resultado = "Reprovado"
else:
    if media < 7:
        resultado = "Exame"
    else:
        resultado = "Aprovado"

print(f"Médias {media:5.2f} - {resultado}!")
