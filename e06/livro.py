class Livro:
    def __init__(self, titulo, ano, autor, editora):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.editora = editora

    def ficha(self):
        # atravessa do livro pro autor e pra editora, igual aos prints da parte 1
        return f"{self.titulo} ({self.ano}) - {self.autor.nome} - {self.editora.nome}"