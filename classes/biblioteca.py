class Biblioteca:

    def __init__(self):

        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):

        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):

        self.usuarios.append(usuario)

    def emprestar_livro(self, titulo, usuario_nome):

        livro = next(
            (l for l in self.livros if l.titulo.lower() == titulo.lower()),
            None
        )

        usuario = next(
            (u for u in self.usuarios if u.nome.lower() == usuario_nome.lower()),
            None
        )

        if not livro:
            print("Livro não encontrado.")
            return

        if not usuario:
            print("Usuário não encontrado.")
            return

        if livro.emprestar():
            print(f"Livro '{livro.titulo}' emprestado para {usuario.nome}.")

        else:
            print("Livro já está emprestado.")

    def devolver_livro(self, titulo):

        livro = next(
            (l for l in self.livros if l.titulo.lower() == titulo.lower()),
            None
        )

        if not livro:
            print("Livro não encontrado.")
            return

        livro.devolver()

        print(f"Livro '{livro.titulo}' devolvido com sucesso.")

    def relatorio_emprestados(self):

        print("\n===== LIVROS EMPRESTADOS =====")

        encontrou = False

        for livro in self.livros:

            if livro.emprestado:

                encontrou = True

                print(f"- {livro.titulo} | {livro.autor}")

        if not encontrou:
            print("Nenhum livro emprestado no momento.")

    def listar_livros(self):

        print("\n===== TODOS OS LIVROS =====")

        if not self.livros:
            print("Nenhum livro cadastrado.")
            return

        for livro in self.livros:

            print(
                f"Título: {livro.titulo} | "
                f"Autor: {livro.autor} | "
                f"Status: {livro.status()}"
            )