matriz = int(input("Digite a ordem da matriz: "))

M = []

for l in range(matriz):
    linha = [] # para cada linha
for c in range(matriz):
    valor = 2 ** (l + c) # esse valor segnifica que o valor da matriz é 2 elevado a soma do índice da linha e coluna
#que o usuario digitou
linha.append(valor)
M.append(linha)

for linha in range(matriz):
    for coluna in range(matriz):
        print(f"{M[linha][coluna]:4d}" , end='')
        print()