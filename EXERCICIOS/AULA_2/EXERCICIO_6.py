#Escreva um programa que deve dizer se um carro é:
#▶ novo (se tem menos de 3 anos)
#▶ velho (mais ou igual a 3 anos)
#A idade do carro deve ser informada pelo usuário
#Observação: Resolva usando apenas Estruturas de Decisão Completas.

Car = int(input("Digite quantos anos o veiculo possui: "))

if Car >= 3:
    print("O seu veículo é antigo!")
else:
    print("O seu veículo é novo!")