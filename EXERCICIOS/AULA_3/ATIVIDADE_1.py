#Escreva um algoritmo que peça para o usuário digitar um número. Se o número for 
#divisível por 5, exiba a mensagem "Múltiplo de 5 detectado!". Caso contrário, o 
#programa não deve exibir nada. Use desvio condicional simples.

Numero = int(input("Digite um numero: "))

if Numero % 5 == 0:
    print("Múltiplo de 5 detectado!")