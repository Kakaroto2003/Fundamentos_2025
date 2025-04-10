# Exercício 5
# Faça um programa que:
# ▶ Imprime uma sequência de n números em ordem inversa à da leitura
# ▶ Utilize uma lista para isso.

Qtd = int(input("Digite a quantidade de números: "))

N = []
for i in range(Qtd):
    num = int(input("Digte um número: "))
    N.append(num)

print(f"\nNumeros: {N}")
print("Inverso:")

for num in reversed(N):
    print(num)



