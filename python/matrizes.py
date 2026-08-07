matriz = [[1, 2, 3],
          [4, 5, 6]]

print(matriz[1], [2], [3]);

for linha in matriz:

  for valor in linha:
    print(valor, end= " ");
print()


matriz = []

for i in range(3):
  linha = [];
for j in range(3):
  valor = int(input(f"valor [{i}][{j}]: "))
  linha.append(valor);
matriz.append(linha);

print(matriz);