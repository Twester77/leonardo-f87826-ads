print("Olá, seja bem-vindo!")
nota = []
nome = []
alunos = []  
notas_final = [] 

for i , j in range(1, 6):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = int(input(f"Digite a nota do aluno {j+1}: "))

    alunos.append((nome, nota))
    notas_final.append(nota)

maior_nota = max(notas_final)
menor_nota = min(notas_final)
media_turma = sum(notas_final) / len(notas_final)

acima_da_media = 0

for nome, nota in alunos:
    if nota > media_turma:
        acima_da_media += 1
        print(f"{nome} tirou {nota} e está ACIMA da média.")
    elif nota < media_turma:
        print(f"{nome} tirou {nota} e está ABAIXO da média.")
    else:
        print(f"{nome} tirou {nota} e está NA média.")

print(f"A maior nota da turma é: {maior_nota}")
print(f"A menor nota da turma é: {menor_nota}")
print(f"A média geral da turma é: {media_turma:.2f}")
print(f"Quantidade de notas acima da média: {acima_da_media}")
