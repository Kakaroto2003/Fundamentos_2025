#Gerar e gravar números pares e ímpares em arquivos separados:
#Números de 0 a 999.
#Números pares no arquivo pares.txt
#Números ímpares no arquivo impares.txt

arquivo_pares = open("pares.txt", "w")
arquivo_impares = open("impares.txt", "w")

for i in range(0, 1000):
    if i % 2 == 0:
        arquivo_pares.write(f"{i}\n")
    else:
        arquivo_impares.write(f"{i}\n")

arquivo_pares.close()  
arquivo_impares.close()

# with open("pares.txt", "w") as arquivo_pares:
#     for i in range(0, 1000):
#         if i % 2 == 0:
#             arquivo_pares.write(f"{i}\n")
# with open("impares.txt", "w") as arquivo_impares:
#     for i in range(0, 1000):
#         if i % 2 != 0:
#             arquivo_impares.write(f"{i}\n")



# with open("pares.txt", "w") as arquivo_pares, open("impares.txt", "w") as arquivo_impares:
#     for i in range(0, 1000):
#         if i % 2 == 0:
#             arquivo_pares.write(f"{i}\n")
#         else:
#             arquivo_impares.write(f"{i}\n")
