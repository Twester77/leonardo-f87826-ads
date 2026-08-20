def cadastrar(acervo, titulo, autor, ano):
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    acervo.append(livro)

def buscar(acervo, titulo):
    for livro in acervo:
        if livro["titulo"] == titulo:
            return livro  # DEVOLVE o livro, nao imprime
    return None  # percorreu tudo e nao achou

def listar(acervo):
    return acervo

if __name__ == "__main__":
    # Teste unitario exigido pelo roteiro
    teste = []
    cadastrar(teste, "Dom Casmurro", "Machado de Assis", 1899)
    print(buscar(teste, "Dom Casmurro"))
    print(buscar(teste, "Nao existe"))