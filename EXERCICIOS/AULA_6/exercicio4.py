# Exercício 4
# Faça um programa que permita imprimir uma represetação de tabela quadrada com $ e @. 
# Nesta tabela o triangulo inferior esquerdo deve ser preenchido com $ e o triângulo superior direito deve ser preenchido com @.

R = int(input("Digite o número de linhas do tabuleiro: "))

for linha in range(R):
    for coluna in range(R):
        if linha <= coluna:
            print("@", end=" ")
        else:
            print("$", end=" ")
    print()