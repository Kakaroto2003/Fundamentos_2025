#Faça um programa que peça dois números. Imprima o menor deles.
# Observação: Resolva usando apenas Estruturas de Decisão Simples.

#Saída esperada:
#Exemplo de execução
#Digite um numero: 5
#Digite outro numero: 30
#Maior: 30

N1 = int(input("Digite um numero: "))
N2 = int(input("Digite outro numero: "))

if N1 > N2:
    print("Maior:", N1)
if N2 > N1:
    print("Maior:", N2)