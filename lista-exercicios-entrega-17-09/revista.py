class Revista:
    def __init__(self, titulo, edicao, ano):
        if not titulo:
            raise ValueError("Titulo e obrigatorio")
        self.titulo = titulo
        self.edicao = edicao
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - n. {self.edicao} ({self.ano})"

    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, valor):
        if valor <= 0:
            raise ValueError(f"Edicao invalida: {valor}")
        self._edicao = valor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > 2026:
            raise ValueError(f"Ano invalido: {valor}")
        self._ano = valor