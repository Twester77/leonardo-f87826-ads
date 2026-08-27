import tkinter as tk

from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

# Dados iniciais (os mesmos do roteiro)
acervo = [
    Livro("Dom Casmurro", "Machado de Assis", 1899),
    Livro("Iracema", "Jose de Alencar", 1865),
    Livro("O Cortico", "Aluisio Azevedo", 1890),
]
emprestimos = []
usuario = Usuario("Aluno", "0000")

# Janela
janela = tk.Tk()
janela.title("Biblioteca")
janela.geometry("460x360")

# Rótulo "Acervo"
tk.Label(janela, text="Acervo", font=("Arial", 14)).pack(pady=6)

# Lista de livros
lista = tk.Listbox(janela, width=52, height=6)
for livro in acervo:
    lista.insert(tk.END, str(livro))
lista.pack(padx=10)

# Campo de digitação
campo = tk.Entry(janela, width=34)
campo.pack(pady=8)

# Rótulo de resultado (será exibido depois dos botões)
resultado = tk.Label(janela, text="", fg="blue")

# Função emprestar
def emprestar():
    procurado = campo.get()
    escolhido = None
    for item in acervo:
        if item.titulo.lower() == procurado.lower():
            escolhido = item
            break

    if escolhido is None:
        resultado.config(text="Nao esta no acervo.", fg="red")
        return

    emprestimo = Emprestimo(escolhido, usuario, "27/08/2026")
    emprestimos.append(emprestimo)
    resultado.config(text="Emprestado: " + str(emprestimo), fg="blue")

# Função devolver
def devolver():
    if not emprestimos:
        resultado.config(text="Nao ha emprestimo.", fg="red")
        return

    emprestimo = emprestimos[-1]   # último emprestado
    try:
        emprestimo.devolver()
        resultado.config(text="Devolvido: " + str(emprestimo), fg="blue")
    except ValueError as erro:
        resultado.config(text=str(erro), fg="red")

# Botões
tk.Button(janela, text="Emprestar", command=emprestar).pack()
tk.Button(janela, text="Devolver", command=devolver).pack(pady=4)

# Exibe o rótulo de resultado (depois dos botões)
resultado.pack(pady=6)

# Mantém a janela aberta
janela.mainloop()