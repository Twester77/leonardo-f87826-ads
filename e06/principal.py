from autor import Autor
from editora import Editora
from livro import Livro
from aluno import Aluno
from emprestimo import Emprestimo

machado = Autor("Machado de Assis", "brasileiro", 1839)
companhia = Editora("Companhia das Letras", "Sao Paulo")
casmurro = Livro("Dom Casmurro", 1899, machado, companhia)
ana = Aluno("2026001", "Ana Souza", "17 99999-00000")
emp = Emprestimo(ana, casmurro, "11/09/2026")

# --- prints da parte 1 ---
print(ana.nome)
print(ana.telefone)
print(emp.data)
print(emp.livro.titulo)
print(emp.livro.autor.nome)
print(emp.livro.editora.cidade)

# --- prints da parte 2 ---
print(casmurro.ficha())
print(machado.apresentacao())
print(companhia.etiqueta())
print(emp.resumo())

# devolve e mostra de novo, o status tem que mudar
emp.devolver()
print(emp.resumo())