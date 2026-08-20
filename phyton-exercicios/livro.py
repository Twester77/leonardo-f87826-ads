class Livro :

 def __init__(self, titulo, autor, ano):
  self.titulo = titulo
  self.autor = autor
  self.ano = ano
    
if not titulo:
         raise ValueError("Titulo é obrigatorio")
if ano < 1450 or ano > 2026:
         raise ValueError(f"ano invalido: {ano}")
        

    
def descricao(self):
 return f"{self.titulo} - {self.autor} ({self.ano})";


def idade(self):
 return 2026 = self.ano

    
    
if __name__== "__main__":
    
 acervo = [
  Livro("Dom Casmurro", "Machado de Assis", 1899),
  Livro("Iracema", "Jose de Alencar", 1865),
  Livro("O Cortico", "Aluisio Azevedo", 1890),
]


for livro in acervo :
 print(Livro.titulo,"-", livro.ano)

 print(livro.descricao(), "-", livro.idade(), "anos")

 print(livro.titulo)
 