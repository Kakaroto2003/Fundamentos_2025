# Exercício 07
# Faça um programa que preencha uma matriz 10 X 3 com as notas de 10 alunos com 3 provas (valores gerados de forma aleatória entre 0 e 10).
# O programa deverá mostrar:
# ▶ A matriz com todas as notas de cada aluno.
# ▶ Um relatório com o número do aluno (número da linha), a prova em que cada aluno obteve a menor nota (número da coluna) e o valor da menor nota.
# ▶ O relatório deverá mostrar também qual foi a menor nota obtida em cada prova e a quantidade de alunos que obtiveram essa menor nota na respectiva prova.

import random  # Importa o módulo 'random' que permite gerar números aleatórios

# Cria uma matriz 10x3 (10 alunos, 3 provas), preenchida com inteiros aleatórios entre 0 e 10
matriz = [[random.randint(0, 10) for _ in range(3)] for _ in range(10)]

# Imprime um título explicando o conteúdo da matriz
print("Notas dos alunos (linha = aluno, coluna = prova):")

# Percorre cada linha da matriz (cada aluno), com o índice 'i' e o conteúdo 'linha'
for i, linha in enumerate(matriz):
    print(f"{i}: {linha}")  # Exibe o número do aluno e suas 3 notas

print()  # Imprime uma linha em branco para separar visualmente as seções do programa

# Relatório que mostra a menor nota de cada aluno
for i, linha in enumerate(matriz):  # Para cada linha da matriz (ou seja, para cada aluno)
    menor_nota = min(linha)         # Calcula a menor nota desse aluno usando a função 'min'
    idx = linha.index(menor_nota)   # Encontra o índice (coluna) onde essa menor nota está
    # Exibe o número do aluno, o valor da menor nota, e em qual coluna (prova) ela ocorreu
    print(f"Aluno {i}: menor nota: {menor_nota}, idx: {idx}")

print()  # Imprime uma linha em branco para separar visualmente as seções do programa

# Relatório que mostra, para cada prova, qual foi a menor nota obtida e quantos alunos a tiraram
for j in range(3):  # Para cada prova (coluna 0, 1 e 2)
    menor = 10  # Inicializa a variável 'menor' com o maior valor possível de nota (10)
    
    # Percorre todas as linhas (alunos) para encontrar a menor nota da prova 'j'
    for i in range(10):
        if matriz[i][j] < menor:  # Se a nota do aluno na prova 'j' for menor que a atual 'menor'
            menor = matriz[i][j]  # Atualiza o valor de 'menor' com essa nota
    
    # Conta quantos alunos tiraram exatamente essa menor nota na prova 'j'
    count = sum(1 for i in range(10) if matriz[i][j] == menor)
    
    # Exibe o número da prova, a quantidade de alunos que tiraram a menor nota, e o valor dessa nota
    print(f"Menor nota na prova {j} = {count} alunos com essa nota: {menor}")
