# Escreva uma função com parâmetros chamada multiplo(x, y).
# ▶ Esta função deve receber dois números
# ▶ Retornar True se o primeiro for múltiplo do segundo número;
# ▶ Retornar False caso contrário.

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

def múltiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
print(f"{x} é múltiplo de {y}? {múltiplo(x, y)}")
