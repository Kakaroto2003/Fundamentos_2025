#Dados três valores A, B e C, verificar se eles podem ser os comprimentos dos lados de um triângulo, se forem, verificar se
#compõem um triângulo equilátero, isósceles ou escaleno. Informar
#se não compuserem nenhum triângulo.
#Dados de entrada: três lados de um suposto triângulo (A, B, C).
#Dados de saída: mensagens: não compõem triângulo, triângulo
#equilátero, triângulo isósceles, triângulo escaleno.#

#• O que é um triângulo?
#figura geométrica fechada de três lados, em que cada um é
#menor que a soma dos outros dois;
#• O que é um triângulo equilátero?
#um triângulo com três lados iguais;
#• O que é um triângulo isósceles?
#um triângulo com dois lados iguais;
#• O que é um triângulo escaleno?
#um triângulo com todos os lados diferentes.

a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))
if (a < b + c) and (b < a + c) and (c < a + b):
    if (a == b) and ( b == c):
        print("Triangulo equilatero")
    else:
        if (a == b) or (a == c) or (b == c):
            print("Triangulo isosceles")
        else:
            print("Triangulo escaleno")
else:
    print("Nao e Triangulo")
