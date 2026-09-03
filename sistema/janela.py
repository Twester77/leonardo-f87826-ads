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



titulo_secao = tk.Label(janela, text="Cadastrar livro",font=("Arial", 12))
titulo_secao.pack(pady=(10,4))
formulario= tk.Frame(janela)
formulario.pack()

tk.Label(formulario, text="Titulo:").grid(row=0, column=0, sticky="e")
campo_titulo = tk.Entry(formulario, width=28)
campo_titulo.grid(row=0, column=1, pady=2)

tk.Label(formulario, text="Autor: ").grid(row=1, column=0, sticky="e")
campo_autor = tk.Entry(formulario, width=28)
campo_autor.grid(row=1, column=1, pady=2)

tk.Label(formulario, text="Ano:").grid(row=2, column=1, sticky="e")
campo_ano = tk.Entry(formulario, width=28)
campo_ano.grid(row=2, column=1, pady=2)


def atualizar_lista():
    lista.delete(0, tk.END)
    for livro in acervo:
        lista.insert(tk.END, str(livro))
        
def cadastrar():
    titulo = campo_titulo.get()
    autor = campo_autor.get()
    ano = campo_ano.get()
    
    try:
        livro = Livro(titulo, autor, int(ano))
        acervo.append(livro)
        atualizar_lista()
        campo_titulo.delete(0, tk.END)
        campo_autor.delete(0, tk.END)
        campo_ano.delete(0, tk.END)
        resultado.config(text="Cadastrado: " + str(livro), fg="green")
        
    except ValueError as erro:
        resultado.config(text=str(erro), fg="red")
            
    

    livro = Livro(titulo, autor, int(ano))
    acervo.append(livro)
    resultado.config(text="Cadastrado: " + str(livro), fg="blue")
    
tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=6, padx=10)
    

# Mantém a janela aberta
janela.mainloop()