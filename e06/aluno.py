class Aluno:
    def __init__(self, ra, nome, telefone):
        self.ra = ra
        self.nome = nome
        self.telefone = telefone

    def primeiro_nome(self):
        # split() separa por espaço e o [0] pega só o primeiro pedaço
        return self.nome.split()[0]