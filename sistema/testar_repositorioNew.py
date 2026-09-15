from dominio.livro import Livro
from dados.repositorio_livro import RepositorioLivro
repositorio = RepositorioLivro()

print("--- o que ja esta guardado --- ")

for livro in repositorio.listar():
    print(livro.id, "-", livro.descricao())

repositorio.fechar()
    