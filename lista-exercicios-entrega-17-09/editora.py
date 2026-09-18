class Editora:
    def __init__(self, nome, cidade, fundacao):
        self.nome = nome
        self.cidade = cidade
        self.fundacao = fundacao

    def idade(self):
        return 2026 - self.fundacao

    def __str__(self):
        return f"{self.nome} - {self.cidade} ({self.fundacao})"

    @property
    def fundacao(self):
        return self._fundacao

    @fundacao.setter
    def fundacao(self, valor):
        if valor < 1500 or valor > 2026:
            raise ValueError(f"Ano de fundacao invalido: {valor}")
        self._fundacao = valor


companhia = Editora("Companhia das Letras", "Sao Paulo", 1986)
print(companhia)
print("Idade:", companhia.idade())