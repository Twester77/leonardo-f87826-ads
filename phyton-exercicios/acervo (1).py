# o acervo e uma lista, e cada item dela e um dicionario
acervo = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "ano": 1938},
    {"titulo": "Grande Sertao", "autor": "Guimaraes Rosa", "ano": 1956},
]

# len() devolve quantos itens a lista tem
print("livros no acervo:", len(acervo))

for livro in acervo:
    print(f'{livro["titulo"]} ({livro["ano"]}) - {livro["autor"]}')

# Agora a busca
procurado = input("Titulo: ")
encontrado = None  # None e a ausencia de valor: "ainda não achei nada"

for livro in acervo:
    if livro["titulo"] == procurado:
        encontrado = livro
        break  # achou: nao precisa percorrer o resto

if encontrado:
    print(f'Autor: {encontrado["autor"]}')
else:
    print("Nao esta no acervo.")