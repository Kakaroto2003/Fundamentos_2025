# Exercício 03
#  Faça um programa para receber uma matriz 3 X 3 (solicitar ao
#  usuário)
#  Apresentar a soma dos elementos da diagonal principal
#  Exemplo de execução:

print("=== MATRIZ 3x3 ===")
print("Digite os 9 valores da matriz (linha por linha):")

# Criando a matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

# Mostrando a matriz de forma organizada
print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

# Calculando a soma da diagonal principal
soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]

print(f"\nSoma dos elementos da diagonal principal: {soma_diagonal}")
