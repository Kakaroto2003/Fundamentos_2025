# Exercício 04
#  Solicitar dados de uma matriz 4 X 4
#  Montar uma lista de 4 elementos com a soma dos elementos
#  ímpares de cada linha da matriz

# Inicializa uma lista vazia que representará a matriz 4x4
matriz = []

# Exibe uma mensagem para o usuário começar a digitar os valores
print("Digite os elementos da matriz 4x4:")

# Laço externo para percorrer as 4 linhas
for i in range(4):
    linha = []  # Inicializa uma lista para armazenar os elementos da linha atual
    # Laço interno para percorrer as 4 colunas
    for j in range(4):
        # Solicita ao usuário um valor inteiro e armazena na variável "valor"
        valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
        # Adiciona o valor digitado na lista da linha
        linha.append(valor)
    # Adiciona a linha completa na matriz
    matriz.append(linha)

# Inicializa uma lista para guardar as somas dos elementos ímpares de cada linha
somas_impares = []

# Percorre cada linha da matriz
for linha in matriz:
    # Cria uma lista com os números ímpares da linha e soma todos eles
    soma = sum([num for num in linha if num % 2 != 0])
    # Adiciona a soma encontrada à lista somas_impares
    somas_impares.append(soma)

# Exibe a matriz completa (linha por linha)
print("\nMatriz 4x4:")
for linha in matriz:
    print(linha)

# Exibe a lista com as somas dos elementos ímpares de cada linha
print("\nSoma dos elementos ímpares de cada linha:")
print(somas_impares)


