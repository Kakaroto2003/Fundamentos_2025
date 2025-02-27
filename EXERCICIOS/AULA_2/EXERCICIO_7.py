#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km
#Calcule o preço da passagem:
#▶ cobrando R$ 0,50 por km para viagens até 200 km
#▶ R$ 0,45 por km para viagens mais longas.
#Observação: Resolva usando apenas Estruturas de Decisão Completas.

Km = float(input("Digite a distância que você deseja percorrer (em km): "))  

if Km <= 200:
    preco = Km * 0.5  
else:
    preco = 200 * 0.5 + (Km - 200) * 0.45  

print("O preço da passagem será: R$ %.2f" % preco) 
