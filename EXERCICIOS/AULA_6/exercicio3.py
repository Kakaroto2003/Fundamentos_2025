# Exercício 3
# Faça um program que permita imprimir uma representação de um tabuleiro de xadrez utilizando os caracteres "o" e "x".
# O canto superior esquerdo do tabuleiro deve ser preenchido com o caractere "o".

T = int(input("Digite o número de linhas do tabuleiro: "))

for linha in range(T):
    for coluna in range(T):
        if (linha + coluna) % 2 == 0:
            print("O", end=" ")
        else:
            print("X", end=" ")
    print()