#Construa um algoritmo que, tendo como dados de entrada o preço
#de um produto e seu código de origem, mostre o preço junto de
#sua procedência. Caso o código não seja nenhum dos
#especificados, o produto deve ser encarado como importado.
#Siga a tabela de códigos:

CO = int(input("Digite o código de Origem: "))

if CO == 1:
    print("O produto é do Sul")
elif CO == 2:
    print("O produto é do Norte")
elif CO == 3:
    print("O produto é do Leste")
elif CO == 4:
    print("O produto é do Oeste")
elif CO == 5 or CO ==6:
    print("O produto é do Nordeste")
elif CO == 7 or CO == 8 or CO == 9:
    print("O produto é do Sudeste")
elif CO >= 10 and CO <= 20:
    print("O produto é do Centro-Oeste")
elif CO >= 25 and CO <= 30:
    print("O produto é do Nordeste")
else:
    print("Origem do produto desconhecida")

