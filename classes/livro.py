class Livro:

    def __init__(self, titulo, autor):

        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def emprestar(self):

        if self.emprestado:
            return False

        self.emprestado = True
        return True

    def devolver(self):

        self.emprestado = False

    def status(self):

        if self.emprestado:
            return "Emprestado"

        return "Disponível"