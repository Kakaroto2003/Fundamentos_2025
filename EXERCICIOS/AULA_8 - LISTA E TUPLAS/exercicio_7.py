# Exercício 7
# As temperaturas de uma cidade foram armazenadas na lista
# temperaturas = [-10,-8, 0, 1, 2, 5,-2,-4].
# Faça um programa que imprime a menor e a maior temperatura
# E imprima também a média das temperaturas

temperaturas = [-10,-8, 0, 1, 2, 5,-2,-4]

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print("Maior:", maior)
print("Menor:", menor)
print(f"Media: {media:.1f}")

