import sqlite3

# o banco é um ARQUIVO. se ele não existir, o connect cria na hora
conexao = sqlite3.connect("biblioteca.db")

# o cursor é quem leva o comando até o banco e traz a resposta de volta
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livro (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT    NOT NULL,
        autor  TEXT,
        ano    INTEGER
    )
""")

print("Tabela criada.")

# cada ? é um buraco que o Python preenche com um valor da tupla, na ordem
cursor.execute(
    "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
    ("Dom Casmurro", "Machado de Assis", 1899)
)

# o desafio do encontro passado: os outros dois de uma vez
outros = [
    ("Iracema", "Jose de Alencar", 1865),
    ("O Cortico", "Aluisio Azevedo", 1890),
]
for titulo, autor, ano in outros:
    cursor.execute(
        "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
        (titulo, autor, ano)
    )

print("Inserido.")

# sem esta linha, nada do que você inseriu chega ao arquivo
conexao.commit()

cursor.execute("SELECT id, titulo, autor, ano FROM livro")

# codigo, e não id: id() já é um comando do Python, não vale a pena apagar
for codigo, titulo, autor, ano in cursor.fetchall():
    print(f"{codigo} - {titulo} - {autor} ({ano})")

conexao.close()
