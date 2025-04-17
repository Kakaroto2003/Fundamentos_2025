# Exercício 6. Escreva uma função Python para encontrar o segundo maior
# elemento em uma lista.

def media(n1, n2, n3, tipo):
    if tipo == 'A':
        return (n1 + n2 + n3) / 3
    elif tipo == 'P':
        return (n1 * 5 + n2 * 3 + n3 * 2) / (5 + 3 + 2)
    else:
        return None  # ou você pode lançar um erro

# Função principal (exemplo de uso):
n1 = float(input())
n2 = float(input())
n3 = float(input())
tipo = input().strip().upper()

resultado = media(n1, n2, n3, tipo)

if resultado is not None:
    print(f"{resultado:.1f}") 