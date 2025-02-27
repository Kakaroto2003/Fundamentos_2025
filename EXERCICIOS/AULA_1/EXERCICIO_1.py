#Faça um programa que leia a altura de uma pessoa e calcule o peso ideal, suponha que o peso ideal seja dado pela fórmula:
#(72.7 × altura) − 58

#digite sua altura: 1.7
#Peso ideal: 65.59

Altura = float(input("Digite sua altura (em metros): "))  # Pede a altura corretamente
Peso_ideal = (72.7 * Altura) - 58  # Cálculo correto

print(f"Seu peso ideal é: {Peso_ideal:.2f} kg")  # Exibe o resultado formatado

