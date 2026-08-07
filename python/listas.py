notas = []
notas.append(7)
notas.append(8.6)
notas.append(6)

print(notas)
print("\n Quantas: ", len(notas));
print("\n Primeira nota: ", notas[0]);
print("\n Ultima nota: ", notas[-1]);
print("\n Soma das notas: ", sum(notas));
print("\n Média das notas: ", sum(notas) / len(notas));
print("\n maior: ", max(notas));


for nota in notas: 
 print("\n", nota)
