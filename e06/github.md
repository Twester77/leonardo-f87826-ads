# Lab E06 — Parte 2: Os métodos

Continuação da Parte 1 (as classes e as ligações).

## O que foi feito nesta parte

Acrescentei os métodos pedidos em cada classe, **sem reescrever nada da Parte 1**:

- `Autor.apresentacao()` → "Machado de Assis (brasileiro, 1839)"
- `Editora.etiqueta()` → "Companhia das Letras - Sao Paulo"
- `Livro.ficha()` → "Dom Casmurro (1899) - Machado de Assis - Companhia das Letras"
- `Aluno.primeiro_nome()` → "Ana"
- `Emprestimo.resumo()` → "Ana Souza pegou Dom Casmurro em 11/09/2026 [em aberto]"
- `Emprestimo.devolver()` → marca `self.devolvido = True`

Também criei o atributo `self.devolvido = False` direto dentro do `__init__`
do `Emprestimo` — ele não vem por parâmetro, pois todo empréstimo nasce em aberto.

## Arquivos

- `autor.py`
- `editora.py`
- `livro.py`
- `aluno.py`
- `emprestimo.py`
- `principal.py`

## Como rodar

Na pasta dos arquivos:
executar python principal.py

## Link do Repositório
https://github.com/Twester77/leonardo-f87826-ads.git