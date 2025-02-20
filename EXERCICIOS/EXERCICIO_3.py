#Faça um programa que solicita do usuário uma quantidade de dias, horas, minutos e segundos. Calcule e imprima o total convertido em somente segundos.

#Exemplo de execucao do programa:

#digite a quantidade de dias: 1
#digite a quantidade de horas: 2
#digite a quantidade de minutos: 10
#digite a quantidade de segundos: 5
#tempo total foi de 94205 segundos

Dias = int(input("Digite a quantidade de dias trabalhados: ")) * 86400
Horas = int(input("Digite a quantidade de horas trabalhadas: ")) * 3600
Minutos = int(input("Digite a quantidade de minutos trabalhados: ")) * 60
Segundos = int(input("Digite a quantidade de segundos trabalhados: "))

Total = Dias + Horas + Minutos + Segundos  # Soma total em segundos

print(f"O tempo total gasto foi: {Total} segundos")
