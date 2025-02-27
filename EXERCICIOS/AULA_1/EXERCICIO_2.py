#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que:

# ▶ o carro custa R$ 60,00 por dia
# ▶ e R$ 0,15 por km rodado.


Km = int(input("Digite a quantidade de quilômetros percorridos: "))
Dias = int(input("Digite a quantidade de dias: "))
Total = (Km * 0.15) + (Dias * 60)

print(f"Total a pagar: R$ {Total:.2f}")

