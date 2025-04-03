

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

def calculo(x, y, z):
    return (x**0.5) + (y**0.5) + (z**0.5) + ((x + y) / 2) + ((y + z) / 2) + ((x + z) / 2)

print (f"O resultado do cálculo é: {calculo(x, y, z)}")