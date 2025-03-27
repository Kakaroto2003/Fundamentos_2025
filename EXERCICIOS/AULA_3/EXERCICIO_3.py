#Tendo como dados de entrada a altura e o sexo de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando
#as seguintes fórmulas:
#▶ para homens: (72,7 * h) - 58;
#▶ para mulheres: (62,1 * h) - 44,7.

Sexo = input("Digite seu sexo (M para masculino e F para feminino): ").strip().upper()
H = float(input("Digite sua Altura: "))

Masc = (72.7*H) - 58
Fem = (62.1*H) - 44.7

if Sexo == "M":
    print(f"Seu peso ideal é: {Masc:.2f} Kg")
else:
    print(f"Seu peso ideal é: {Fem:.2f} Kg")
    
