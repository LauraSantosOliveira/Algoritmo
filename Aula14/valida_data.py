from datetime import datetime

def valida_data(n):
    d = int(n[0:2])
    m = int(n[3:5])
    a = int(n[6:10])

    if not (1 <= d <= 31) or not (1 <= m <= 12) or not (1900 <= a <= 9999):
        return False

    data_nasc = datetime(a, m, d).date()
    hoje = datetime.now().date()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

    return idade >= 18

dat = str(input("Digite a sua data de nascimento no formado dd/mm/aaaa: "))

print(valida_data(dat))
