# Use a função criada no exercício anterior
# Exiba todas as datas mágicas do século XX. Ou seja, do ano 1901 à 2000

def magica(dia, mes, ano):
    if dia * mes % 100:
        return True
    else:
        return False

for ano in range (1901, 2001):
    for mes in range (1, 13):
        for dia in range(1, 32):
           if magica(dia, mes, ano) == True:
             print(f"Data mágica: {dia}/{mes}/{ano}")    



    