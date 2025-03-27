# Exercício 3
# Faça um program que permita imprimir uma representação de um tabuleiro de xadrez utilizando os caracteres "o" e "x".
# O canto superior esquerdo do tabuleiro deve ser preenchido com o caractere "o".

L = int(input("Digite o número de linhas do retângulo: "))
C = int(input("Digite o número de colunas do retângulo: "))

for linha in range(L):
    for coluna in range(C):
        if (linha + coluna) % 2 ==0:
            print("O", end=" ")
        else:
            print("X", end=" ")
    print()