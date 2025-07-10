"""Elabore um programa em python que leia valores inteiros para preencher uma matriz A 5 x 5.
Você deverá criar adicionalmente dois vetores de 5 elementos: somaLinhas e
somaColunas. Em cada posição do vetor somaLinhas deverá ser armazenada a soma da
linha correspondente na matriz A. Da mesma forma, em cada posição do vetor
somaColunas deverá ser armazenada a soma da coluna correspondente na matriz A."""

# Criação da matriz 5x5
A = []
for i in range(5):
    A.append([]) 
    for j in range(5):
        valor = int(input(f"Digite o valor para A[{i}][{j}]: "))
        A[i].append(valor)

# Vetores para armazenar as somas
somaLinhas = [0, 0, 0, 0, 0]
somaColunas = [0, 0, 0, 0, 0]

# Cálculo das somas
for i in range(5):
    for j in range(5):
        somaLinhas[i] += A[i][j]      # Soma da linha i, no caso sempre vai adicionar pra linha i os elementos que a compoe
        somaColunas[j] += A[i][j]     # Soma da coluna j, mesma coisa para coluna j

# Impressão da matriz (opcional)
print("\nMatriz A:")
for linha in A:
    print(linha)

# Saida dos resultados
print("\nSoma das linhas:", somaLinhas)
print("Soma das colunas:", somaColunas)
