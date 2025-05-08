#Crie um arquivo: “numeros.txt” que contenha 100 números aleatórios;
#Escreva uma função que leia uma sequência numérica do arquivo “numeros.txt” e salva os números na lista num.
# Escreva outra função que recebe a lista num como parâmetro e retorna uma nova lista num_unicos, sem os elementos repetidos.
#Escreva uma terceira função que recebe a lista num_unicos e grava os números no arquivo “numeros_unicos.txt”.

from random import randint

def main():
    gerar_numeros("numeros.txt")
    numeros = ler_numeros("numeros.txt")
    numeros_unicos = numeros_unicos(numeros)
    salvar_numeros_unicos("numeros_unicos.txt", numeros_unicos)

def gerar_numeros(arquivo):
    with open("numeros.txt", "w") as arquivo:
        for i in range(1, 101):
            arquivo.write(f"{randint(1, 100)} ")

def ler_numeros(arquivo):
    with open(arquivo, "r") as arq:
        numeros = arq.readlines()
        lista = []
        for numero in numeros:
            lista.append(int(numero.strip()))
    return lista

def numeros_unicos(lista):
    lista_unicos = []
    for numero in lista:
        if numero not in lista_unicos:
            lista_unicos.append(numero)
    return lista_unicos

def salvar_numeros_unicos(arquivo, lista_unicos):
    with open(arquivo, "w") as arq:
        for numero in lista_unicos:
            arq.write(f"{numero} ")


if __name__ == "__main__":
    main()
