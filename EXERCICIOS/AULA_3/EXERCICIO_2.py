#Escreva um algoritmo que leia três valores inteiros e
#diferentes e mostre-os em ordem decrescente.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

if A>B and A>C:
    print(A)
elif B>A and B>C:
    print(B)
else:
    print(C)

if A>B and A<C or A<B and A>C:
    print(A)
elif B>A and B<C or B<A and A>C:
    print(B)
else:
    print(C)
    
if A<B and A<C:
    print(A)
elif B<A and B<C:
    print(B)
else:
    print(C)


