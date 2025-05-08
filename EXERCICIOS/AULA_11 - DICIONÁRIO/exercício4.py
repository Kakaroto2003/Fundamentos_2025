# Exercício 4. Crie uma função que retorna o número de caracteres únicos em uma string criada pelo usuário.
# Por exemplo:
# “Hello, World!” tem 10 caracteres únicos
# enquanto zzz tem somente 1 caractere único.
# Use um dicionário para resolver este problema.

def contar_caracteres_unicos(string):
    dicionario = {}
    for char in string:
        if char not in dicionario:
            dicionario[char] = 1
        else:
            dicionario[char] += 1
    return len(dicionario)

# Programa principal
string_usuario = input("Digite uma string: ")
