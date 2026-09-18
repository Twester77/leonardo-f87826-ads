class Emprestimo:
    def __init__(self, aluno, livro, data):
        self.aluno = aluno
        self.livro = livro
        self.data = data
        self.devolvido = False   # nasce em aberto, não vem por parâmetro

    def resumo(self):
        status = "devolvido" if self.devolvido else "em aberto"
        return f"{self.aluno.nome} pegou {self.livro.titulo} em {self.data} [{status}]"

    def devolver(self):
        self.devolvido = True