# Exercício 5
# Faça um programa que permita imprimir uma representação da tabela quadrada seguindo o padrão. 

T = int(input("Digite o número de linhas do tabuleiro: "))

for linha in range(T):
    for coluna in range(T):
        if linha % 2 == 0 and coluna % 2 == 0:
            print("X", end=" ")
        elif linha % 2 == 0 and coluna % 2 == 1:
            print("O", end=" ")
        elif linha % 2 == 1 and coluna % 2 == 0:
            print("$", end=" ")
        elif linha % 2 == 1 and coluna % 2 == 1:
            print("&", end=" ")
    print()