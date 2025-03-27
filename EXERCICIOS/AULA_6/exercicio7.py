# Exercício 7
# Crie um porgama que permita verificar se um número pertence a sequência de Fibonacci.
# A sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores.
# Entrada: O programa recebe um número inteiro, N, maior que zero.
# Saída: O programa deve imprimir "verdadeiro" se o número N pertence ou "Falso" caso não pertença à sequência de Fibonacci.

N = int(input('Digite um número para saber se ele pertence a sequência de Fibonacci!: '))
a=0
b=1
#a, b = 0, 1

while a <= N:
    if a == N:
        print("Esse número pertence a sequência de Fibonacci!")
        break
    c = a + b
    a = b
    b = c
    #a, b = b, a + b

if a > N:
    print("Esse número não faz parte da sequência de Fibonacci.")