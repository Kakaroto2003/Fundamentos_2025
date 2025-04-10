# Exercício 2
# Faça um programa que:
# ▶ Mostre o menor valor dentro da lista T = [11, 7, 2, 4]

T = [11, 7, 2, 4]
menor = float("inf")

for elemento in T:
    if elemento < menor:
        menor = elemento
print("O menor valor da lista T é:", menor".")


# Ou

T = [11, 7, 2, 4]

menor_valor = min(T)
print(f"O menor valor da lista T é: {menor_valor}.")