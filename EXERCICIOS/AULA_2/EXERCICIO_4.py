#Escreva um programa que pergunte o salário de um funcionário
#Calcule o valor do aumento de salário sabendo que:
#▶ Para salários superiores a R$ 1250,00 calcule um aumento de 10%.
#▶ Para salários inferiores ou iguais a R$ 1250,00, aumento de 15%.
#Imprima o novo salário.
#Observação: Resolva usando apenas Estruturas de Decisão Completas.

Sal = int(input("Digite o seu salario: "))

if Sal > 1250:
    print("Seu novo salario será:", Sal*1.1)
else:
    print("Seu novo salario será:", Sal*1.15)