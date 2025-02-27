#Faça um programa que pergunte quanto a pessoa ganha por hora e o número de horas trabalhas no mês. Calcule e mostre o total
#do salário no referido mês, sabendo-se que são descontados 11% para o imposto de renda, 8% para o INSS e 5% para o sindicato.

#Saída esperada:

#Exemplo de execuçao do programa:

#Digite o valor da hora de trabalho: 50
#Digite o numero de horas trabalhadas no mes: 80

#+ Salario Bruto: R$ 4000.00
#- IR (11%): R$ 440.00
#- INSS (8%): R$ 320.00
#- Sindicato (5%): R$ 200.00
#+ Salario liquido: R$ 3040.00

# Entradas do usuário
Valor_Hora = float(input("Digite o valor da hora trabalhada: "))
Valor_Mes = int(input("Digite o número de horas trabalhadas no mês: "))


Salario_Bruto = Valor_Hora * Valor_Mes

IR = Salario_Bruto * 0.11  # 11% de imposto de renda
INSS = Salario_Bruto * 0.08  # 8% de contribuição para o INSS
Sindicato = Salario_Bruto * 0.05  # 5% de contribuição sindical


Salario_Liquido = Salario_Bruto - (IR + INSS + Sindicato)

print(f"Salário Bruto: R$ {Salario_Bruto:.2f}")
print(f"Desconto IR (11%): R$ {IR:.2f}")
print(f"Desconto INSS (8%): R$ {INSS:.2f}")
print(f"Desconto Sindicato (5%): R$ {Sindicato:.2f}")
print(f"Salário Líquido: R$ {Salario_Liquido:.2f}")

