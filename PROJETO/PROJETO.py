MENU_USUARIO = {
    1: "Buscar Música",
    2: "Curtir Música",
    3: "Descurtir Música",
    4: "Ver Histórico",
    5: "Gerenciar Playlists",
    0: "Voltar"
}

USUARIOS_ARQ = "usuarios.txt"
MUSICAS_ARQ = "musicas.txt"
HISTORICO_ARQ = "historico.txt"
PLAYLISTS_ARQ = "playlists.txt"


def main():
    print("\nBem-vindo ao Spotifei!")
    while True:
        print("\n1 - Cadastrar novo usuário")
        print("2 - Login")
        print("0 - Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            usuario = login()
            if usuario:
                menu_usuario(usuario)
        elif escolha == "0":
            print("\nEncerrando programa...")
            print("Volte sempre!\n")
            break
        else:
            print("Opção inválida!")


def cadastrar_usuario():
    nome = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    try:
        with open(USUARIOS_ARQ, "r", encoding="utf-8") as arq:
            for linha in arq:
                u, _ = linha.strip().split(",")
                if nome == u:
                    print("\nNome de usuário já existe! Tente outro.")
                    return
    except FileNotFoundError:
        pass

    with open(USUARIOS_ARQ, "a", encoding="utf-8") as arq:
        arq.write(f"{nome},{senha}\n")

    print("\nUsuário cadastrado com sucesso!")


def login():
    nome = input("\nNome de usuário: ").strip()
    senha = input("Senha: ").strip()

    try:
        with open(USUARIOS_ARQ, "r", encoding="utf-8") as arq:
            for linha in arq:
                u, s = linha.strip().split(",")
                if nome == u and senha == s:
                    print("\nLogin bem-sucedido!")
                    return nome
    except FileNotFoundError:
        pass

    print("\nUsuário ou senha inválidos.")
    return None


def menu_usuario(usuario):
    while True:
        print("\n=== Menu do Usuário ===\n")
        for k, v in MENU_USUARIO.items():
            print(f"{k} - {v}")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            buscar_musica(usuario)
        elif opcao == "2":
            curtir_musica(usuario)
        elif opcao == "3":
            descurtir_musica(usuario)
        elif opcao == "4":
            ver_historico(usuario)
        elif opcao == "5":
            gerenciar_playlists(usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def buscar_musica(usuario):
    nome = input("Digite o nome da música: ").strip().lower()
    encontrado = False

    try:
        with open(MUSICAS_ARQ, "r", encoding="utf-8") as arq:
            for linha in arq:
                if linha.strip() == "":
                    continue
                try:
                    titulo, artista = [x.strip() for x in linha.strip().split(",")]
                    if nome in titulo.lower():
                        print(f"Música encontrada: {titulo} - {artista}")
                        with open(HISTORICO_ARQ, "a", encoding="utf-8") as hist:
                            hist.write(f"{usuario},buscou,{titulo} - {artista}\n")
                        encontrado = True
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")
        return

    if not encontrado:
        print("Música não encontrada.")


def curtir_musica(usuario):
    nome = input("\nDigite o nome da música que deseja curtir: ").strip().lower()
    opcoes = []

    try:
        with open(MUSICAS_ARQ, "r", encoding="utf-8") as arq:
            for linha in arq:
                if linha.strip():
                    try:
                        titulo, artista = [x.strip() for x in linha.strip().split(",")]
                        if nome in titulo.lower():
                            opcoes.append((titulo, artista))
                    except ValueError:
                        continue
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")
        return

    if not opcoes:
        print("Nenhuma música encontrada.")
        return
    elif len(opcoes) == 1:
        titulo, artista = opcoes[0]
        with open(HISTORICO_ARQ, "a", encoding="utf-8") as hist:
            hist.write(f"{usuario},curtiu,{titulo} - {artista}\n")
        print("Música curtida com sucesso!")
    else:
        print("\nMúsicas encontradas:\n")
        for i, (titulo, artista) in enumerate(opcoes, start=1):
            print(f"{i} - {titulo} - {artista}")
        escolha = input("\nDigite o número da música que deseja curtir: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            titulo, artista = opcoes[int(escolha)-1]
            with open(HISTORICO_ARQ, "a", encoding="utf-8") as hist:
                hist.write(f"{usuario},curtiu,{titulo} - {artista}\n")
            print("Música curtida com sucesso!")
        else:
            print("Opção inválida.")


def descurtir_musica(usuario):
    nome = input("\nDigite o nome da música que deseja descurtir: ").strip().lower()
    opcoes = []

    try:
        with open(MUSICAS_ARQ, "r", encoding="utf-8") as arq:
            for linha in arq:
                if linha.strip():
                    try:
                        titulo, artista = [x.strip() for x in linha.strip().split(",")]
                        if nome in titulo.lower():
                            opcoes.append((titulo, artista))
                    except ValueError:
                        continue
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")
        return

    if not opcoes:
        print("Nenhuma música encontrada.")
        return
    elif len(opcoes) == 1:
        titulo, artista = opcoes[0]
        with open(HISTORICO_ARQ, "a", encoding="utf-8") as hist:
            hist.write(f"{usuario},descurtiu,{titulo} - {artista}\n")
        print("Música descurtida com sucesso!")
    else:
        print("\nMúsicas encontradas:")
        for i, (titulo, artista) in enumerate(opcoes, start=1):
            print(f"{i} - {titulo} - {artista}")
        escolha = input("\nDigite o número da música que deseja descurtir: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            titulo, artista = opcoes[int(escolha)-1]
            with open(HISTORICO_ARQ, "a", encoding="utf-8") as hist:
                hist.write(f"{usuario},descurtiu,{titulo} - {artista}\n")
            print("Música descurtida com sucesso!")
        else:
            print("Opção inválida.")


def ver_historico(usuario):
    curtidas = []
    descurtidas = []

    try:
        with open(HISTORICO_ARQ, "r", encoding="utf-8") as arq:
            for linha in arq:
                try:
                    u, acao, musica = linha.strip().split(",", 2)
                    if u == usuario:
                        if acao == "curtiu":
                            curtidas.append(musica)
                        elif acao == "descurtiu":
                            descurtidas.append(musica)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Nenhum histórico encontrado.")
        return

    print(f"\n=== Histórico de {usuario} ===")

    if curtidas:
        print("\nMúsicas Curtidas:")
        for m in curtidas:
            print(f"  - {m}")
    else:
        print("\nNenhuma música curtida.")

    if descurtidas:
        print("\nMúsicas Descurtidas:")
        for m in descurtidas:
            print(f"  - {m}")
    else:
        print("\nNenhuma música descurtida.")



def gerenciar_playlists(usuario):
    while True:
        print("\n--- Gerenciar Playlists ---\n")
        print("1 - Criar nova playlist")
        print("2 - Deletar playlist")
        print("3 - Adicionar música à playlist")
        print("4 - Remover música da playlist")
        print("5 - Ver minhas playlists")
        print("0 - Voltar\n")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da nova playlist: ").strip()
            with open(PLAYLISTS_ARQ, "a", encoding="utf-8") as f:
                f.write(f"{usuario},{nome},\n")
            print("Playlist criada com sucesso!")

        elif escolha == "2":  # Deletar playlist
            playlist = input("Nome da playlist que deseja deletar: ").strip()
            linhas = []
            deletada = False

            try:
                with open(PLAYLISTS_ARQ, "r", encoding="utf-8") as f:
                    for linha in f:
                        partes = linha.strip().split(",", 2)
                        if not (len(partes) == 3 and partes[0] == usuario and partes[1] == playlist):
                            linhas.append(linha)
                        else:
                            deletada = True
            except FileNotFoundError:
                pass

            if deletada:
                with open(PLAYLISTS_ARQ, "w", encoding="utf-8") as f:
                    f.writelines(linhas)
                print("Playlist deletada com sucesso!")
            else:
                print("Playlist não encontrada.")

        elif escolha == "3":  # Adicionar música
            playlist = input("Nome da playlist: ").strip()
            nome = input("Digite parte do nome da música que deseja adicionar: ").strip().lower()
            opcoes = []

            try:
                with open(MUSICAS_ARQ, "r", encoding="utf-8") as arq:
                    for linha in arq:
                        if linha.strip():
                            try:
                                titulo, artista = [x.strip() for x in linha.strip().split(",")]
                                if nome in titulo.lower():
                                    opcoes.append(f"{titulo} - {artista}")
                            except ValueError:
                                continue
            except FileNotFoundError:
                print("Arquivo de músicas não encontrado.")
                continue

            if not opcoes:
                print("Nenhuma música encontrada.")
                continue
            elif len(opcoes) == 1:
                musica = opcoes[0]
            else:
                print("\nMúsicas encontradas:")
                for i, m in enumerate(opcoes, start=1):
                    print(f"{i} - {m}")
                escolha_musica = input("Digite o número da música: ")
                if escolha_musica.isdigit() and 1 <= int(escolha_musica) <= len(opcoes):
                    musica = opcoes[int(escolha_musica) - 1]
                else:
                    print("Opção inválida.")
                    continue

            linhas = []
            atualizada = False

            try:
                with open(PLAYLISTS_ARQ, "r", encoding="utf-8") as f:
                    for linha in f:
                        partes = linha.strip().split(",", 2)
                        if len(partes) == 3 and partes[0] == usuario and partes[1] == playlist:
                            nova_linha = f"{partes[0]},{partes[1]},{partes[2]}{musica};"
                            linhas.append(nova_linha + "\n")
                            atualizada = True
                        else:
                            linhas.append(linha)
            except FileNotFoundError:
                pass

            if atualizada:
                with open(PLAYLISTS_ARQ, "w", encoding="utf-8") as f:
                    f.writelines(linhas)
                print("Música adicionada com sucesso!")
            else:
                print("Playlist não encontrada.")

        elif escolha == "4":  # Remover música
            playlist = input("Nome da playlist: ").strip()
            nome = input("Digite parte do nome da música que deseja remover: ").strip().lower()
            opcoes = []

            try:
                with open(MUSICAS_ARQ, "r", encoding="utf-8") as arq:
                    for linha in arq:
                        if linha.strip():
                            try:
                                titulo, artista = [x.strip() for x in linha.strip().split(",")]
                                if nome in titulo.lower():
                                    opcoes.append(f"{titulo} - {artista}")
                            except ValueError:
                                continue
            except FileNotFoundError:
                print("Arquivo de músicas não encontrado.")
                continue

            if not opcoes:
                print("Nenhuma música encontrada.")
                continue
            elif len(opcoes) == 1:
                musica = opcoes[0]
            else:
                print("\nMúsicas encontradas:")
                for i, m in enumerate(opcoes, start=1):
                    print(f"{i} - {m}")
                escolha_musica = input("Digite o número da música: ")
                if escolha_musica.isdigit() and 1 <= int(escolha_musica) <= len(opcoes):
                    musica = opcoes[int(escolha_musica) - 1]
                else:
                    print("Opção inválida.")
                    continue

            linhas = []
            atualizada = False

            try:
                with open(PLAYLISTS_ARQ, "r", encoding="utf-8") as f:
                    for linha in f:
                        partes = linha.strip().split(",", 2)
                        if len(partes) == 3 and partes[0] == usuario and partes[1] == playlist:
                            musicas = partes[2].split(";")
                            musicas = [m for m in musicas if m and m.strip() != musica]
                            nova_linha = f"{usuario},{playlist},{';'.join(musicas)};"
                            linhas.append(nova_linha + "\n")
                            atualizada = True
                        else:
                            linhas.append(linha)
            except FileNotFoundError:
                pass

            if atualizada:
                with open(PLAYLISTS_ARQ, "w", encoding="utf-8") as f:
                    f.writelines(linhas)
                print("Música removida com sucesso!")
            else:
                print("Playlist não encontrada ou música não estava presente.")

        elif escolha == "5":  # Ver playlists
            print("\n--- Minhas Playlists ---\n")
            try:
                with open(PLAYLISTS_ARQ, "r", encoding="utf-8") as f:
                    for linha in f:
                        partes = linha.strip().split(",", 2)
                        if len(partes) == 3 and partes[0] == usuario:
                            nome = partes[1]
                            musicas = partes[2].strip(';').split(';') if partes[2] else []
                            print(f"Playlist: {nome}\n")
                            for m in musicas:
                                print(f"  - {m}\n")
            except FileNotFoundError:
                print("Nenhuma playlist encontrada.")

        elif escolha == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()