# Crie um programa que inverta a ordem das linhas do arquivo pares.txt.
# A primeira linha deve conter o maior número e a última linha o menor.
# Salve o resultado em outro arquivo (invertido.txt).

with open("pares.txt", "w") as arquivo:
    for i in range(0, 1002):
        if i % 2 == 0:
            arquivo.write(f"{i}\n")

with open("pares.txt", "r") as arquivo:
    linhas = arquivo.readlines()

linhas_invertidas = linhas[::-1]
with open("invertido.txt", "w") as arquivo_invertido:
    for linha in linhas_invertidas:
        arquivo_invertido.write(linha)
    

