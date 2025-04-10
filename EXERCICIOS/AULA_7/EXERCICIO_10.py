# Refaça os exercícios 3, 4, e 5 utilizando função lambda

def maximo (x, y):
    if x > y:
        return x
    else:
        return y
    
maximo = lambda x, y: x if x > y else y

def múltiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
múltiplo = lambda x, y: True if x % y == 0 else False

def area_triangulo(base, altura):

    return (base * altura) / 2

area_triangulo = lambda base, altura: (base * altura) / 2