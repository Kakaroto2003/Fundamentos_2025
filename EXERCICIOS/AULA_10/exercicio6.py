# Exercício 06

# Cria uma matriz m[12][12] com números inteiros aleatórios. Em seguida, calcule e mostre a soma ou a média considerando
# somente aqueles elementos que estão abaixo da diagonal principal da matriz, conforme ilustrado abaixo (área verde).
# A entrada do programa deve ser um único caractere maiúsculo ’S’ ou ’M’, indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz.

# Importa o módulo random para gerar números inteiros aleatórios
import random

# Cria uma matriz 12x12 preenchida com números aleatórios entre 0 e 100
# Usamos compreensão de listas para criar a matriz
# Para cada uma das 12 linhas, geramos uma lista com 12 números aleatórios
matriz = [[random.randint(0, 100) for _ in range(12)] for _ in range(12)]

# Solicita ao usuário que digite a operação desejada
# 'S' para Soma ou 'M' para Média
# .strip() remove espaços extras e .upper() transforma em letra maiúscula
operacao = input("Digite 'S' para Soma ou 'M' para Média dos elementos abaixo da diagonal principal: ").strip().upper()

# Inicializa a variável que irá guardar a soma dos elementos
soma = 0

# Inicializa a variável que irá contar quantos elementos foram somados
quantidade = 0

# Percorre as linhas da matriz (i de 0 a 11)
for i in range(12):
    # Percorre as colunas até antes da diagonal principal (j de 0 até i-1)
    for j in range(i):
        # Adiciona o valor do elemento atual à variável soma
        soma += matriz[i][j]
        # Incrementa a quantidade de elementos somados
        quantidade += 1

# Exibe a matriz completa formatada
print("\nMatriz 12x12:")
# Para cada linha da matriz
for linha in matriz:
    # Imprime os elementos da linha separados por espaço
    print(" ".join(str(num) for num in linha))

# Verifica qual operação o usuário escolheu
if operacao == 'S':
    # Se for 'S', exibe a soma dos elementos abaixo da diagonal principal
    print(f"\nSoma dos elementos abaixo da diagonal principal: {soma}")
elif operacao == 'M':
    # Se for 'M', calcula a média dos elementos abaixo da diagonal
    # Garante que não haja divisão por zero (caso quantidade seja 0)
    media = soma / quantidade if quantidade > 0 else 0
    # Exibe a média com duas casas decimais
    print(f"\nMédia dos elementos abaixo da diagonal principal: {media:.2f}")
else:
    # Se o usuário digitou algo diferente de 'S' ou 'M', exibe mensagem de erro
    print("\nOperação inválida! Use 'S' para soma ou 'M' para média.")
