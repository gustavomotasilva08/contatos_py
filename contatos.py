
contatos = {}

while True:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("4 - Remover contato")
    print("5 - Editar contato")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")

        contatos[nome] = telefone

        print("Contato adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do contato: ")

        if nome in contatos:
            print(f"Telefone de {nome}: {contatos[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        if contatos:
            print("\n=== LISTA DE CONTATOS ===")

            for nome, telefone in contatos.items():
                print(f"{nome} - {telefone}")
        else:
            print("Nenhum contato cadastrado.")

    elif opcao == "4":
        nome = input("Digite o nome do contato que deseja remover")