# Exercício 6
# Faça um programa para criar uma lista de 10 elementos inteiros
# ▶ Mostre todos os elementos que forem maiores que a soma de dois de seus antecessores

L = []
for i in range (10):
    valor = int(input(f"Digite um número: "))
    L.append(valor)

for i in range(2, len(L)):
    if L[i] > (L[i-1] + L[i-2]):
        print(f'{L[i]}')
