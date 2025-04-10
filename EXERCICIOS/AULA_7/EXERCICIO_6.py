# Faça um programa que:
# ▶ Leia três números e apresente o resultado do seguinte cálculo:
# √n1 + √n2 + √n3 + ((n1 + n2)/2) + ((n2 + n3)/2) + ((n1 + n3)/2)

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

def calculo(x, y, z):

    """
    Calcula com base na fórmula do exercicio 6

    Args:
        x (int): Primeiro número
        y (int): Segundo número
        z (int): Terceiro número

    returns:
        float: Resultado do cálculo

    """
    return (x**0.5) + (y**0.5) + (z**0.5) + ((x + y) / 2) + ((y + z) / 2) + ((x + z) / 2)

print (f"O resultado do cálculo é: {calculo(x, y, z)}")