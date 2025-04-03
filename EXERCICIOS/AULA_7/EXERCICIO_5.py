#Escreva uma função com parâmetros que:
# ▶ Receba a base e a altura de um triângulo e retorne sua área

base = int(input("Digite a base do triangulo: "))
altura = int(input("Digite a altura do triangulo: "))

def area_triangulo(base, altura):

    return (base * altura) / 2
    
    
print(f"A área do triandulo é {area_triangulo(base, altura)}")
