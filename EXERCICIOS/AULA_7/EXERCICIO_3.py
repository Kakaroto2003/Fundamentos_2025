x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

def maximo (x, y):
    if x > y:
        return x
    else:
        return y

print(f"O maior número entre {x} e {y} é {maximo(x, y)}")