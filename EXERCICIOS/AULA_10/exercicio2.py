# Exercício 02
#  Faça um programa que cria uma matriz M 10 X 15, sendo que cada
#  elemento é um inteiro gerado aleatoriamente.
#  Então, exiba a matriz completa e, na sequência, somente os
#  elementos da primeira coluna da matriz.

from random import randint

# Criar a matriz M 10x15 com valores inteiros aleatórios entre 0 e 99
linhas = 10
colunas = 15
M = [[random.randint(0, 100) for _ in range(colunas)] for _ in range(linhas)]

# Exibir a matriz completa
print("\nMatriz completa:\n")
for linha in M:
    print(linha)

# Exibir apenas os elementos da primeira coluna
print("\nElementos da primeira coluna:\n")
for linha in M:
    print(linha[0])
