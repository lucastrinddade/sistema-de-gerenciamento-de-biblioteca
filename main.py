from classes.livro import Livro
from classes.usuario import Usuario
from classes.biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:

    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Relatório de livros emprestados")
    print("6 - Listar todos os livros")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")

        livro = Livro(titulo, autor)

        biblioteca.cadastrar_livro(livro)

        print("Livro cadastrado com sucesso!")

    elif opcao == "2":

        nome = input("Nome do usuário: ")

        usuario = Usuario(nome)

        biblioteca.cadastrar_usuario(usuario)

        print("Usuário cadastrado com sucesso!")

    elif opcao == "3":

        titulo = input("Digite o título do livro: ")
        usuario_nome = input("Digite o nome do usuário: ")

        biblioteca.emprestar_livro(titulo, usuario_nome)

    elif opcao == "4":

        titulo = input("Digite o título do livro: ")

        biblioteca.devolver_livro(titulo)

    elif opcao == "5":

        biblioteca.relatorio_emprestados()

    elif opcao == "6":

        biblioteca.listar_livros()

    elif opcao == "0":

        print("\nStatus final dos livros:")
        biblioteca.listar_livros()

        print("\nSistema encerrado.")
        break

    else:

        print("Opção inválida!")