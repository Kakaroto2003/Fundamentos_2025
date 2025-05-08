# Crie uma agenda de telefones que salva os dados de maneira permanente.
# A agenda deve funcionar em loop infinito, até que o usuário decida sair. Os dados armazenados são: nome, sobrenome, telefone e e-mail.
# A agenda deve apresentar o seguinte menu para o usuário:
# ▶ 1 - Novo contato (create)
# ▶ 2 - Procura (pelo nome) (read)
# ▶ 3 - Atualiza contato (update)
# ▶ 4 - Apaga contato (delete)
# ▶ 0 - Sair

#with open("agenda.txt", "a") as arquivo:
#    while True:
#        print("\nMenu:\n")

#        print("1 - Novo contato")
#        print("2 - Procura (pelo nome)")                                                                                    
#        print("3 - Atualiza contato")
#        print("4 - Apaga contato")
#        print("0 - Sair\n")
#
#        opcao = input("Escolha uma opção: ")
#        if opcao == "1":
#            nome = input("Digite o nome: ")
#            sobrenome = input("Digite o sobrenome: ")
#            telefone = input("Digite o telefone: ")
#            email = input("Digite o e-mail: ")

#            with open("agenda.txt", "a") as arquivo:
#                arquivo.write(f"{nome},{sobrenome},{telefone},{email}\n")
#            print("Contato adicionado com sucesso!")

#        elif opcao == "2":
#            nome_procurado = input("Digite o nome a ser procurado: ")
#            encontrado = False
#            with open("agenda.txt", "r") as arquivo:
#                for linha in arquivo.readlines():
#                    nome, sobrenome, telefone, email = linha.strip().split(",")
#                    if nome == nome_procurado:
#                        print(f"Nome: {nome}\nSobrenome: {sobrenome}\nTelefone: {telefone}\nE-mail: {email}\n")
#                        encontrado = True
#                        break
#            if not encontrado:
#                print("Contato não encontrado.")

#        elif opcao == "3":
#            nome_atualizar = input("Digite o nome do contato a ser atualizado: ")
#            contatos = []
#            encontrado = False
#            with open("agenda.txt", "r") as arquivo:
#                for linha in arquivo.readlines():
#                    contato = linha.strip().split(",")
#                    if contato[0] == nome_atualizar:
#                        novo_nome = input("Novo nome: ")
#                        novo_sobrenome = input("Novo sobrenome: ")
#                        novo_telefone = input("Novo telefone: ")
#                        novo_email = input("Novo e-mail: ")
#                        contatos.append([novo_nome, novo_sobrenome, novo_telefone, novo_email])
#                        encontrado = True
#                    else:
#                        contatos.append(contato)
#            if encontrado:
#                with open("agenda.txt", "w") as arquivo:
#                    for contato in contatos:
#                        arquivo.write(",".join(contato) + "\n")
#                print("Contato atualizado com sucesso!")
#            else:
#                print("Contato não encontrado.")

#        elif opcao == "4":
#            nome_apagar = input("Digite o nome do contato a ser apagado: ")
#            contatos = []
#            encontrado = False
#            with open("agenda.txt", "r") as arquivo:
#                for linha in arquivo.readlines():
#                    contato = linha.strip().split(",")
#                    if contato[0] != nome_apagar:
#                        contatos.append(contato)
#                    else:
#                        encontrado = True
#            if encontrado:
#                with open("agenda.txt", "w") as arquivo:
#                    for contato in contatos:
#                        arquivo.write(",".join(contato) + "\n")
#                print("Contato apagado com sucesso!")
#            else:
#                print("Contato não encontrado.")
#        elif opcao == "0":
#            print("Saindo da agenda...")
#            break
#        else:
#            print("Opção inválida! Tente novamente.")

MENU = {
    1: "Novo contato",
    2: "Procurar contato", 
    3: "Atualizar contato",
    4: "Apagar contato",
    0: "Sair"
}

def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            novo_contato()
        elif opcao == 2:
            procurar_contato()
        elif opcao == 3:
            atualizar_contato()
        elif opcao == 4:
            apagar_contato()
        elif opcao == 0:
            sair()
            break
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu():
    for opcao, descricao in MENU.items():
            print(f"{opcao} - {descricao}")

def novo_contato():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    with open("agenda.txt", "a") as arquivo:
        arquivo.write(f"{nome},{sobrenome},{telefone},{email}\n")

    print("Contato adicionado com sucesso!")

def procurar_contato():
    nome_procurado = input("Digite o nome do contato que deseja procurar: ")
    
    with open("conatatos.txt", "r") as arquivo:
        contatos = arquivo.readlines()
    
    for contato in contatos:   
        nome, sobrenome, telefone, email = contato.strip().split(",")
        if nome.lower9() == nome_procurado.lower():
            print(f"Nome: {nome}\nSobrenome: {sobrenome}\nTelefone: {telefone}\nE-mail: {email}")
            break
    else:
        print("Contato não encontrado.")

def atualizar_contato():
    nome_procurado = input("Digite o nome do contato que deseja atualizar: ")

    with open("contatos.txt", "r") as arquivo:
        contatos = arquivo.readlines()

    for i, contato in enumerate(contatos):
        nome, sobrenome, telefone, email = contato.strip().split(",")
        if nome.lower() == nome_procurado.lower():
            novo_nome = input("Novo nome: ")
            novo_sobrenome = input("Novo sobrenome: ")
            novo_telefone = input("Novo telefone: ")
            novo_email = input("Novo e-mail: ")

            contatos[i] = f"{novo_nome},{novo_sobrenome},{novo_telefone},{novo_email}\n"
            break

def apagar_contato():
    nome_procurado = input("Digite o nome do contato que deseja apagar: ")

    with open("contatos.txt", "r") as arquivo:
        contatos = arquivo.readlines()

    for i, contato in enumerate(contatos):
        nome, sobrenome, telefone, email = contato.strip().split(",")
        if nome.lower() == nome_procurado.lower():
            print(f"Contato encontrado: {contato.strip()}")
            contatos.pop(i)
            break
    else:
        print("Contato não encontrado.")

    with open("contatos.txt", "w") as arquivo:
        arquivo.writelines(contatos)
    print("Contato apagado com sucesso!")
    
def sair():
    print('Saindo do programa...')
    exit()

if __name__ == "__main__":
    main()
