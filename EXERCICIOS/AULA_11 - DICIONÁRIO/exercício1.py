#  1.Exercício Escreva uma função chamada procuraChave que encontre todas as
# chaves, em um dicionário, que estão associadas a um valor específico.

# A função receberá o dicionário e o valor a procurar como seus únicos parâmetros.
# A função retornará uma lista (possivelmente vazia) de chaves
# associadas ao valor fornecido.
# Faça um programa principal que mostra o funcionamento da função.
# Seu programa principal deve criar um dicionário e mostrar que
# a função procuraChave funciona corretamente quando retorna
# várias chaves, uma única chave ou nenhuma chave.

def procuraChave(dicionario, valor):
    chaves = []
    for chave, val in dicionario.items():
        if val == valor:
            chaves.append(chave)
    return chaves

dicionario = {
    "Alpha": 1,
    "Bravo": 2,
    "Charlie": 1,
    "Delta": 3,
    "": 4,
    "Echo": 1,
}

print(procuraChave(dicionario, 1))
print(procuraChave(dicionario, 2))
print(procuraChave(dicionario, 3))
print(procuraChave(dicionario, 4))

