# Exercício 2. Uma empresa de pesquisas precisa tabular os resultados da
# seguinte enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o
# resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0,
# que encerra a entrada dos dados. Não deverão ser aceitos
# valores além dos válidos para o programa (0 a 6). Os valores
# referentes a cada uma das opções devem ser armazenados num
# vetor. Após os dados terem sido completamente informados, o
# programa deverá calcular a percentual de cada um dos
# concorrentes e informar o vencedor da enquete. O formato da
# saída foi dado pela empresa, e é o seguinte:

# O Sistema Operacional mais votado foi o Unix, com 3500 votos,
# correspondendo a 40% dos votos.


sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * 6 # [0-6]

# Leitura dos votos
voto = -1
while voto != 0:
    voto = int(input("Digite o código do sistema (1 a 6, 0 para encerrar): "))
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
    elif voto != 0:
        print("Código inválido. Digite um número entre 1 e 6.")


total_votos = sum(votos)
print("Sistema Operacional   Votos    %")
print("---------------------------------")

for i in range(6):
    percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
    print(f"{sistemas[i]:<20}  {votos[i]:<6}  {percentual:.0f}%")

print("---------------------------------")
print(f"{'Total':<20}  {total_votos:<6}")

# Encontrar o sistema mais votado
mais_votado = max(votos)
indice_mais_votado = votos.index(mais_votado)
porcentagem = (mais_votado / total_votos) * 100 if total_votos > 0 else 0

print(f"\nO Sistema Operacional mais votado foi o {sistemas[indice_mais_votado]}, com {mais_votado} votos, correspondendo a {porcentagem:.0f}% dos votos.")
