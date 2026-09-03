from datetime import date

class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("Título é obrigatório")
        if not autor:
            raise ValueError("Autor é obrigatório")
        self.ano = ano
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self._ano})"

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > date.today().year:
            raise ValueError("Ano inválido: {valor}")
        self._ano = valor

    def idade(self):
        return date.today().year - self._anopython.janelapy

    def e_classico(self):
        return self.idade() > 100


class Usuario:
    def __init__(self, nome, matricula):
        if not nome:
            raise ValueError("Nome é obrigatório")
        if not matricula:
            raise ValueError("Matrícula é obrigatória")
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.devolvido = False  

    def __str__(self):
        status = "devolvido" if self.devolvido else "em aberto"
        return f"{self.livro.titulo} -> {self.usuario.nome} ({status})"

    def devolver(self):
        if self.devolvido:
            raise ValueError("Este empréstimo já foi devolvido")
        self.devolvido = True


if __name__ == "__main__":
    livro = Livro("Dom Casmurro", "Machado de Assis", 1899)
    print(livro)   

    try:
        livro.ano = 3000
    except ValueError as e:
        print(f"Erro capturado: {e}")

    usuario = Usuario("Ana Souza", "2026001")
    emprestimo = Emprestimo(livro, usuario, "20/08/2026")

    print(emprestimo)   

    print(emprestimo.livro.autor)      
    print(emprestimo.usuario.matricula) 

    emprestimo.devolver()
    print(emprestimo)   

    try:
        emprestimo.devolver()
    except ValueError as e:
        print(f"Erro esperado: {e}")