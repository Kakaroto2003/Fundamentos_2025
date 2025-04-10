# Exercício 1
# Faça um programa que:
# - Leia 5 valores do usuário e armazene-os em uma lista
# - Imprima a lista completa
# - Imprima o primeiro e o último elemento da lista

vlr1 = int(input("Digite o primeiro valor: "))
vlr2 = int(input("Digite o segundo valor: "))
vlr3 = int(input("Digite o terceiro valor: "))
vlr4 = int(input("Digite o quarto valor: "))
vlr5 = int(input("Digite o quinto valor: "))

L = [vlr1, vlr2, vlr3, vlr4, vlr5]

print("Lista completa:", L)
print("O primeiro número da lista é:", L[0])
print("O último número da lista é:", L[-1])

# Ou

L = []
for i in range (5):
    valor = int(input(f"Digite um valor: "))
    L.append(valor)

print("Lista completa:", L)
print("O primeiro número da lista é:", L[0])
print("O último número da lista é:", L[-1])