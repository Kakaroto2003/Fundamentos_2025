# Exercício 8
# Neste exercício, você criará um programa que lê palavras do usuário até que o usuário entre com uma linha em branco.
# Após o usuário digitar uma linha em branco, seu programa deve exibir cada palavra digitada pelo usuário exatamente uma vez.
# As palavras devem ser exibidas na mesma ordem em que foram inseridas.

P = []

while True:
    palavra = input("Digite uma palavra: ")
    if palavra == "":
        break
    if palavra not in P:
        P.append(palavra)

print("\nPalavras Digitadas: ")
for palavra in P:
    print(palavra)
