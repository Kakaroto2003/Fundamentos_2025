# Duas alternativas, uma para verdadeiro e outra para falso

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4
print("Sua media %.2f" % media)

if media >=5:
 print(" Voce foi aprovado!")
else:
 print(" Voce foi reprovado!")
