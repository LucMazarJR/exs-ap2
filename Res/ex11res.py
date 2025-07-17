"""Elabore um programa em python, para ler valores e armazená-los em uma matriz 5 x 5. Após o
programa deverá responder se a matriz é ou não uma matriz simétrica. Uma matriz
simétrica possui a mesma composição de valores abaixo e acima da diagonal principal."""

# Criação da matriz 5x5
N = 5
matriz = []

print("Digite os valores da matriz 5x5:")

for i in range(N):
    linha = []
    for j in range(N):
        valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Verificação de simetria
simetrica = True

for i in range(N):
    for j in range(i + 1, N):  # Só verifica acima da diagonal principal
        if matriz[i][j] != matriz[j][i]: # As posições simétricas
            simetrica = False
            break

# Resultado
if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz NÃO é simétrica.")
