# Exercício 3
# Faça um programa que:
# ▶ Peça 10 números reais do usuário.
# ▶ Armazene-os em uma lista e diga qual o índice do maior e seu valor

L = []
for i in range (10):
    valor = int(input(f"Digite um valor: "))
    L.append(valor)

maior = float("-inf")
indice_maior = -1
for i in range(len(L)):
    if L[i] > maior:
        maior = L[i]
        indice_maior = i

print(L)
print("Maior número: ", maior)
print(f"O indice do maior número é: {indice_maior}")

# Ou

L = []
for i in range (10):
    valor = float(input(f"Digite um valor: "))
    L.append(valor)

maior = max(L)
indice_maior = L.index(maior)

print(L)
print("Maior número: ", maior)
print(f"O indice do maior número é: {indice_maior}")
