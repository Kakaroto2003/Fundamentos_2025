# Exercício 1. Faça um programa que leia uma quantidade indeterminada de
# números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada
# de dados deverá terminar quando for lido um número negativo

intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0


while True:
    n = int(input("Digite um número positivo (ou negativo para sair): "))
    if n < 0:
        break
    elif n <= 25:
        intervalo_1 += 1
    elif n <= 50:
        intervalo_2 += 1
    elif n <= 75:
        intervalo_3 += 1
    elif n <= 100:
        intervalo_4 += 1
    else:
        print("Numero fora dos parâmetros especificados (0-100)")

print(f'Intervalo [0-25]: {intervalo_1}')
print(f'Intervalo [26-50]: {intervalo_2}')
print(f'Intervalo [51-75]: {intervalo_3}')
print(f'Intervalo [76-100]: {intervalo_4}')
