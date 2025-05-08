# Crie um arquivo: “numeros.txt” que contenha 100 números aleatórios;
# Todos os números do arquivo estão na mesma e única linha, separados por espaço;
# Escreva uma função em Python para retornar a somatória de todos os números que estão armazenados no arquivo “numeros.txt”.

from random import randint

with open("numero.txt", "w") as arquivo:
    for i in range(1, 101):
        arquivo.write(f"{randint(1, 100)} ")

def somar_numeros(arquivo):
    with open(arquivo, "r") as arq:
        numeros = arq.read().strip().split(" ")
        soma = 0
        for numero in numeros:
            soma += int(numero)
    return soma

soma = somar_numeros("numero.txt")
print(f"A soma dos números no arquivo é: {soma}")