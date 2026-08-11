print("Olá, seja bem vindo!");

nota = []
nome = []
alunos = []

for i in range (6):
nome = str(input(f"Digite o nome do aluno {i+1}: "));
nota = int(input(f"Digite a nota do aluno {i+1}: "));
alunos.append((nome, nota))


maior_nota = 

for i in range (1):
     print(f"A soma de a + b + c + d + e é: {n1 + n2 + n3 + n4 + n5 + n6}");
     print(f"A média da turma é: {(n1 + n2 + n3 + n4 + n5 + n6) / 6}");


    
  


 for i in range (1):
     print(f"A soma de a + b + c + d + e é: {n1 + n2 + n3 + n4 + n5 + n6}");
     print(f"A média da turma é: {(n1 + n2 + n3 + n4 + n5 + n6) / 6}");
     
if nota > media :
     print(f"As médias de ({a}||{b}||{c}||{d}||{e}||{f})s ão acima da media", nome.append(str));
     nota.apppend = input(int(nota))
 
elif nota < media : 
     print(f"As médias de ({a}||{b}||{c}||{d}||{e}||{f}) são abaixo da média", nome.append(str));
     nota.apppend = input(int(nota))
else :
     print(f"As médias de ({a}||{b}||{c}||{d}||{e}||{f}) estão dentro da média", nome.append(str));
     nota.apppend = input(int(nota))



print("Olá, seja bem-vindo!")

alunos = []  # Vai guardar o par (nome, nota)
notas_puras = []  # Vai guardar apenas as notas para os cálculos de maior/menor

# LOOP 1: Coleta os dados dos 6 alunos de forma automática
for i in range(6):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = int(input(f"Digite a nota do aluno {i+1}: "))

    # Faz o BIND dos dados salvando na lista de tuplas
    alunos.append((nome, nota))
    # Salva a nota isolada na outra lista para os cálculos
    notas_puras.append(nota)

# Cálculos automáticos (Sem precisar de loop para isso!)
maior_nota = max(notas_puras)
menor_nota = min(notas_puras)
media_turma = sum(notas_puras) / len(notas_puras)

acima_da_media = 0

print("\n--- ANÁLISE DOS ALUNOS ---")
# LOOP 2: Passa por cada aluno guardado para verificar a situação individual
for nome, nota in alunos:
    if nota > media_turma:
        acima_da_media += 1
        print(f"{nome} tirou {nota} e está ACIMA da média.")
    elif nota < media_turma:
        print(f"{nome} tirou {nota} e está ABAIXO da média.")
    else:
        print(f"{nome} tirou {nota} e está NA média.")

# Exibindo os resultados finais solicitados no Exercício 2
print("\n--- RESULTADOS FINAIS ---")
print(f"A maior nota da turma é: {maior_nota}")
print(f"A menor nota da turma é: {menor_nota}")
print(f"A média geral da turma é: {media_turma:.2f}")
print(f"Quantidade de notas acima da média: {acima_da_media}")
