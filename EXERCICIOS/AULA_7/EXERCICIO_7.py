sexo = int(input("Digite o sexo (1) Masculino (2) Feminino: "))
peso = float(input("Digite o peso (kg): "))

def apto_para_doar(sexo, peso):
    if (sexo == 2 and peso >= 50) or (sexo == 1 and peso >= 60):
        return "Apto(a) para doar sangue."
    else:
        return "Não apto(a) para doar sangue."


print(apto_para_doar(sexo, peso))
