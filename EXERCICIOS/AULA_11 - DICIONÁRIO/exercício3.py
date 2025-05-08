# Exercício 3. Neste exercício, você simulará 1000 lançamentos de dois dados.
# Comece escrevendo uma função que simula o lançamento de um par de dados de seis lados cada.
# Sua função não deve aceitar nenhum parâmetro. Ela retornará a somatória obtida pelos dois dados.
# Escreva um programa principal que use sua função para simular 1000 lançamentos de dois dados.

# Como acontece em alguns programas, você deve contar o número de vezes que cada somatória acontece.
# Em seguida, a função principal deve exibir uma tabela que resume esses resultados.
# Mostre a frequência para cada resultado como uma porcentagem do número total de lançamentos.

import random

def lancar_dados():
    dado1 = random.randint(1, 6)                                    # Lança o primeiro dado
    dado2 = random.randint(1, 6)                                    # Lança o segundo dado
    return dado1 + dado2                                            # Retorna a soma dos resultados

lancamentos = {

}

for i in range(100000):                                               # Simula 1000 lançamentos
    resultado = lancar_dados()                                      # Lança os dados
    if resultado not in lancamentos:                                # Se o resultado não estiver no dicionário
        lancamentos[resultado] = 1                                  # Adiciona o resultado ao dicionário com valor 1
    else:
        lancamentos[resultado] += 1                                 # Se o resultado já estiver no dicionário, incrementa o valor em 1

print(lancamentos)
print("\nFrequência de cada resultado:")
for resultado, frequencia in lancamentos.items():                   # Percorre o dicionário
    porcentagem = (frequencia / 100000) * 100                         # Calcula a porcentagem
    print(f"Soma {resultado}: {frequencia} ({porcentagem:.2f}%)")   # Exibe o resultado e a porcentagem





                                      


