# Uma data é considerada mágica quando o dia multiplicado pelo
# mês é igual ao ano de dois dígitos. Por exemplo, 10 de junho de 1960 é uma data mágica porque
# junho é o sexto mês e 6 vezes 10 é 60, o que equivale ao ano de dois dígitos.
# Escreva uma função que determine se uma data é ou não uma data mágica.
# Exemplo:

# Saída esperada                 Saída esperada
# digite o dia: 12               digite o dia: 6
# digite o mes: 2                digite o mes: 10
# digite o ano: 1924             digite o ano: 1960
# Data mágica: 12/2/1924         Data mágica: 6/10/1960

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

def magica(dia, mes):
    if dia * mes % 100:
        return True
    else:
        return False

if magica(dia, mes) == True:
    print(f"Data mágica: {dia}/{mes}/{ano}")

