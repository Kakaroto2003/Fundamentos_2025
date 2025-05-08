# Exercício 2. Faça um programa que gere 100 números aleatórios
# Gere números no intervalo de 0 à 20 - Mostre quantas vezes cada número apareceu
# Dica:
# Utilize um dicionário para armazenar o número como chave
# e a quantidade de vezes em que ele aparece como valor

from random import randint, random

dicionario = {
}

for i in range(100):
    numero = randint(0, 20)
    if numero not in dicionario:
        dicionario[numero] = 1
    else:
        dicionario[numero] = +1

for numero, quantidade in dicionario.items():
    print(f"O número {numero} apareceu {quantidade} vezes.")


