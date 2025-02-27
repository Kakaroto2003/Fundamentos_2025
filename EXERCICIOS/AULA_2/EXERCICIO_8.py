#Escreva um programa que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilíndricos de combustível, em que são fornecidos a altura e o raio do cilindro. Sabendo que:
#▶ O preço da lata de tinta é de acordo com a quantidade:
#⋆ Na compra de 1 lata o valor unitário é de R$ 50,00
#⋆ Na compra de 2 latas o valor unitário é de R$ 48,00
#⋆ Na compra de 3 latas o valor unitário é de R$ 46,00
#⋆ Na compra de mais que 3 latas o valor unitário é de R$ 45,00
#▶ Uma lata de tinta tem 5 litros
#▶ Um litro cobre 3ms
#▶ A área do cilindro é a área da base somada com a área da lateral
#▶ A área da base é π × r2 (r = raio, π = 3.1415)
#▶ A área da lateral é altura multiplicada pelo perímetro
#▶ O perímetro é 2 × π × r

#Utilize os seguintes exemplos para testar:
 
#Altura: 1                                        Altura: 2                                 Altura: 3
#Raio: 1                                          Raio: 2                                   Raio: 3
#Área a ser pintada: 9.42                         Área a ser pintada: 37.70                 Área a ser pintada: 84.82
#Qtde de litros necessários: 3.14                 Qtde de litros necessários: 12.57         Qtde de li lata: R$ 45.00
#Custo total: R$ 50.00                            Custo total: R$ 138.00                    Custo total: R$ 270.tros necessários: 28.27
#Qtde de latas de tinta: 1                        Qtde de latas de tinta: 3                 Qtde de latas de tinta: 6
#Preço unitário da lata: R$ 50.00                 Preço unitário da lata: R$ 46.00          Preço unitário da00

import math  # Importando a biblioteca para usar o valor de π

# Entrada do usuário
altura = float(input("Digite a altura do cilindro (em metros): "))
raio = float(input("Digite o raio do cilindro (em metros): "))

# Cálculo da área do cilindro
area_base = math.pi * (raio ** 2)  
perimetro = 2 * math.pi * raio  
area_lateral = altura * perimetro 
area_total = area_base + area_lateral

# Cálculo da quantidade de tinta necessária
litros_necessarios = area_total / 3  
latas_necessarias = math.ceil(litros_necessarios / 5)  # Arredondando para cima, pois só vendemos latas inteiras

# Definição do preço unitário conforme a quantidade de latas
if latas_necessarias == 1:
    preco_unitario = 50.00
if latas_necessarias == 2:
    preco_unitario = 48.00
if latas_necessarias == 3:
    preco_unitario = 46.00
if latas_necessarias >=4:
    preco_unitario = 45.00


custo_total = latas_necessarias * preco_unitario


print("\nÁrea a ser pintada: %.2f m²" % area_total)
print("Quantidade de litros necessários: %.2f L" % litros_necessarios)
print("Quantidade de latas de tinta: %d" % latas_necessarias)
print("Preço unitário da lata: R$ %.2f" % preco_unitario)
print("Custo total: R$ %.2f" % custo_total)
