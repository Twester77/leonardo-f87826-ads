from acervo import cadastrar, buscar, listar

livros = []

while True:
    print()
    print("=== BIBLIOTECA ===")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Listar")
    print("0 - Sair")
    opcao = input("Opcao: ")

    if opcao == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        try:
            ano = int(input("Ano: "))
        except ValueError:
            print("O ano precisa ser um numero. Tente de novo.")
            continue
        cadastrar(livros, titulo, autor, ano)
        print("Livro cadastrado.")

    elif opcao == "2":
        titulo_busca = input("Buscar titulo: ")
        achado = buscar(livros, titulo_busca)
        if achado:
            print(f'Autor: {achado["autor"]} | Ano: {achado["ano"]}')
        else:
            print("Nao esta no acervo.")

    elif opcao == "3":
        if not livros:
            print("Acervo vazio.")
        else:
            print(f"Total de livros: {len(livros)}")
            for livro in listar(livros):
                print(f'- {livro["titulo"]} ({livro["ano"]}) - {livro["autor"]}')

    elif opcao == "0":
        print("Ate logo.")
        break

    else:
        print("Opcao invalida.")