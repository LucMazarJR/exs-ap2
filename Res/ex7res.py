"""Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos sao da forma: 
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i^2 - 1 se i = j;
A[i][j] = 4i^3 - 5j^2 + 1 se i > j.
"""

# Criação da matriz 10x10
A = []

# Esse tipo de exercicio se refere i e j aos indices da matriz, então só montar a matriz
for i in range(10):
    linha = []
    for j in range(10):
        if i < j:
            valor = 2 * i + 7 * j - 2
        elif i == j:
            valor = 3 * (i ** 2) - 1
        else:  # i > j
            valor = 4 * (i ** 3) - 5 * (j ** 2) + 1
        linha.append(valor)
    A.append(linha)

# Impressão da matriz
for linha in A:
    print(linha)
