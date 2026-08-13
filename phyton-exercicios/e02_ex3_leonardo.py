matriz = []
soma_total = 0

print("Digite os valores para a matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\n--- Resultados ---")
for i, linha in enumerate(matriz):
    soma_linha = sum(linha)
    soma_total += soma_linha
    print(f"Soma da linha {i + 1}: {soma_linha}")

print(f"Soma total da matriz: {soma_total}")