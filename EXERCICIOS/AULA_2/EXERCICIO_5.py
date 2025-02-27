#Escreva um programa que pergunte o ano atual e o ano de nascimento do usuário.
#Calcule a idade dele.
#Se a idade for maior ou igual a 18 anos, mostre uma mensagem dizendo que ele pode tirar CNH.
#Observação: Resolva usando apenas Estruturas de Decisão Simples.

Ano = int(input("Digite o Ano Atual: "))
Ano_N = int(input("Digite o Ano do seu Nascimento: "))

Idade = Ano-Ano_N

if Idade >= 18:
    print("Voce pode tirar CNH!")
if Idade < 18:
    print("Voce não pode tirar CNH!")