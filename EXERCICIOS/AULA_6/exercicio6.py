# Exercício 6
# Crie um progama que leia um número natural positivo N e determine quantos dígitos possui o número.
# Entrada: O programa recebe um número inteiro, N, maior que zero. 
# Saída: O programa deve imprimir a quantidade de dígitos do número N.

N = int(input("Digite um número inteiro: "))

digitos = 0
while N > 0:
    N = N // 10
    digitos = digitos + 1
    print(N)

print(f"O número possui {digitos} digitos!")