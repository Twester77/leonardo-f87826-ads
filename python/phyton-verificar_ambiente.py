"""
Verificação do ambiente — Programação para Desktop e Web · UNIFEV 2026/2

Rode este arquivo para saber se a máquina está pronta para a disciplina.

    python verificar_ambiente.py       (Windows)
    python3 verificar_ambiente.py      (Linux)

Não instala nada. Só confere e diz o que fazer se faltar algo.
"""

import sys

OK = "  [ OK ]"
FALHA = "  [FALHA]"
AVISO = "  [AVISO]"

problemas = []


def titulo(texto):
    print()
    print(texto)
    print("-" * len(texto))


print("=" * 58)
print("  VERIFICACAO DO AMBIENTE — Prog. Desktop e Web · 2026/2")
print("=" * 58)

# ---------------------------------------------------------------- Python
titulo("1. Versao do Python")

v = sys.version_info
print(f"  Versao encontrada: {v.major}.{v.minor}.{v.micro}")
print(f"  Executavel: {sys.executable}")

if v.major < 3:
    print(FALHA, "Python 2 nao serve. Instale o Python 3.")
    problemas.append("Instalar Python 3")
elif v.minor < 10:
    print(FALHA, f"Python 3.{v.minor} e antigo demais. Instale o 3.12 ou mais novo.")
    problemas.append("Atualizar o Python para 3.12 ou mais novo")
elif v.minor < 12:
    print(AVISO, f"Python 3.{v.minor} funciona para esta UC. Atualize quando puder.")
else:
    print(OK, "Versao adequada. Nada a fazer.")

# ---------------------------------------------------------------- tkinter
titulo("2. tkinter — a interface grafica (a partir do encontro 7)")

try:
    import tkinter

    print(OK, f"tkinter disponivel. Tcl/Tk versao {tkinter.TkVersion}")

    # abrir uma janela de verdade: no laboratorio, importar pode funcionar
    # e a janela nao abrir (sem servidor grafico / sessao remota)
    try:
        janela = tkinter.Tk()
        janela.withdraw()
        janela.destroy()
        print(OK, "Consegue abrir janela.")
    except Exception as erro:
        print(FALHA, f"Importa, mas nao abre janela: {erro}")
        problemas.append("tkinter importa mas nao abre janela (ambiente grafico)")

except ModuleNotFoundError:
    print(FALHA, "tkinter NAO esta instalado.")
    if sys.platform.startswith("linux"):
        print("         Linux:   sudo apt install python3-tk")
    elif sys.platform == "win32":
        print("         Windows: reinstale o Python marcando 'tcl/tk and IDLE'")
    else:
        print("         macOS:   instale o Python de python.org (nao o do sistema)")
    problemas.append("Instalar tkinter")

# ---------------------------------------------------------------- sqlite3
titulo("3. sqlite3 — o banco de dados (a partir do encontro 9)")

try:
    import sqlite3

    print(OK, f"sqlite3 disponivel. SQLite versao {sqlite3.sqlite_version}")

    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE teste (id INTEGER PRIMARY KEY, nome TEXT)")
    con.execute("INSERT INTO teste (nome) VALUES (?)", ("funcionou",))
    (resultado,) = con.execute("SELECT nome FROM teste").fetchone()
    con.close()
    print(OK, f"Criou tabela, inseriu e leu: '{resultado}'")

except Exception as erro:
    print(FALHA, f"Problema no sqlite3: {erro}")
    problemas.append("Verificar sqlite3")

# ---------------------------------------------------------------- pip
titulo("4. pip — instalador de bibliotecas (a partir do encontro 21)")

try:
    import pip

    print(OK, f"pip disponivel (versao {pip.__version__}).")
except ModuleNotFoundError:
    print(AVISO, "pip nao encontrado como modulo.")
    print("         Teste no terminal:  python -m pip --version")
    print("         Linux, se faltar:   sudo apt install python3-pip")

# ---------------------------------------------------------------- escrita
titulo("5. Permissao de escrita na pasta")

try:
    with open("_teste_escrita.tmp", "w", encoding="utf-8") as arquivo:
        arquivo.write("ok")

    import os

    os.remove("_teste_escrita.tmp")
    print(OK, "Consegue criar e apagar arquivo nesta pasta.")
except Exception as erro:
    print(FALHA, f"Nao consegue escrever aqui: {erro}")
    print("         O banco de dados precisa gravar em disco.")
    print("         Trabalhe em outra pasta (Documentos, por exemplo).")
    problemas.append("Sem permissao de escrita na pasta de trabalho")

# ---------------------------------------------------------------- resumo
print()
print("=" * 58)
if problemas:
    print("  PENDENCIAS ENCONTRADAS:")
    for numero, item in enumerate(problemas, start=1):
        print(f"    {numero}. {item}")
    print()
    print("  Avise o professor. Nao deixe para a proxima aula.")
else:
    print("  TUDO CERTO. Maquina pronta para o semestre.")
print("=" * 58)