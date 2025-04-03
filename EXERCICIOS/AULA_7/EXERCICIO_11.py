# Faça uma função que receba quatro valores: I, A, B e C.
#Destes valores, I é um valor inteiro valendo 1, 2 ou 3. A, B e C são valores reais. 
# Escreva os números A, B e C obedecendo à tabela a seguir, dependendo do valor de I

i = int(input("Digite a ordem das numerações (1) Crescente - (2) Decrescente - (3) Maior entre os dois números: "))
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

def maximo(a, b, c):
    return max(a, b, c)

def minimo(a, b, c):
    return min(a, b, c)

def meio(a, b, c):
    return a + b + c - maximo(a, b, c) - minimo(a, b, c)  

if i == 1:
    print(minimo(a, b, c), meio(a, b, c), maximo(a, b, c))  
elif i == 2:
    print(maximo(a, b, c), meio(a, b, c), minimo(a, b, c))  
elif i == 3:
    print(minimo(a, b, c), maximo(a, b, c), meio(a, b, c))  
else:
    print("Opção inválida.")

       
    