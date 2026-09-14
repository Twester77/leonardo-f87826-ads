from autor import Autor
from editora import Editora
from livro import Livro
from aluno import Aluno
from emprestimo import Emprestimo

# Criação dos objetos de dentro para fora
machado = Autor("Machado de Assis", "brasileiro", 1839)
companhia = Editora("Companhia das Letras", "Sao Paulo")
casmuro = Livro("Dom Casmurro", 1899, machado, companhia)
ana = Aluno("2026001", "Ana Souza", "17 99999-00000")
emp = Emprestimo(ana, casmuro, "11/09/2026")

# Os seis prints pedidos
print("Nome do aluno:", ana.nome)
print("Telefone do aluno:", ana.telefone)
print("Data do empréstimo:", emp.data)
print("Título do livro:", emp.livro.titulo)
print("Nome do autor do livro:", emp.livro.autor.nome)
print("Cidade da editora do livro:", emp.livro.editora.cidade)