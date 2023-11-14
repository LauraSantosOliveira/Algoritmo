from datetime import datetime

hoje = datetime.now().date()

dat = str(input("Digite a data de nascimento (no formato: dd/mm/aaaa): "))
d = int(dat[0:2])
m = int(dat[3:5])
a = int(dat[6:10])
data_nasc = datetime(a, m, d).date()
idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
print(data_nasc)
print(idade)

if idade < 18:
    print("Data de nascimento inválida")
else:
    print("Data de nascimento válida")
