from revista import Revista

print("---- testando a classe Revista ----")

r = Revista("Superinteressante", 450, 2024)
print("Criada:", r)

try:
    Revista("", 450, 2024)
    print("FALHOU: aceitou titulo vazio")
except ValueError as erro:
    print("ok, barrou:", erro)

try:
    Revista("Piaui", 0, 2024)
    print("FALHOU: aceitou edicao 0")
except ValueError as erro:
    print("ok, barrou:", erro)

try:
    Revista("Piaui", 200, 3000)
    print("FALHOU: aceitou ano 3000")
except ValueError as erro:
    print("ok, barrou:", erro)