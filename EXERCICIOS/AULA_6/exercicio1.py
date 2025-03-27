# Exercício 1
# Faça um programa que receba uma série de numeros naturais e contabilize quantos desses números são primos. 
# Um número primo x é primo se x > 1 e seus únicos divisores são 1 e x.

numero = int(input("Digite um número: "))

primos=0
for i in range(numero):
    n = int(input("Digite um número a ser testado: "))
    eh_primo = True
    if n > 1:
        for j in range(2,n):
            if n % j == 0:
                eh_primo = False
    if eh_primo == True:
        print("É primo")
        primos = primos + 1
    else:
        print("Não é primo")

print(f"A quantidade de primos éa {primos} de {numero} números")