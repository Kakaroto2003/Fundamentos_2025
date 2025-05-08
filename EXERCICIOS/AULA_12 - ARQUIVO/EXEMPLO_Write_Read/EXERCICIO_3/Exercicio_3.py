#Utilize o arquivo “pares.txt” gerado no último exemplo:
#Vamos criar outro arquivo que deve conter somente os números múltiplos de 4

nome = input("Digite o nome: ")

while nome != "":
    telefone = input("Digite o telefone: ")
    with open("contatos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{telefone}\n")
    nome = input("Digite o nome: ")

with open("contatos.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha.strip().split(","))

# with open("contatos.txt", "r") as arquivo:
#     for linha in arquivo.readlines():
#         nome, telefone = linha.strip().split(",")
#         print(f"Nome: {nome}, Telefone: {telefone}")