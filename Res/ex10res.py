"""Escreva um programa que leia um número inteiro N, depois um caractere maiúsculo 
(S para soma ou M para média) e em seguida leia os N x N números de uma matriz. 
Calcule a soma ou a média dos elementos que estão acima da diagonal principal da matriz 
e imprima o resultado com uma casa decimal."""



N = int(input())           # Tamanho da matriz
operacao = input().strip()  # 'S' ou 'M'

matriz = []

# Leitura da matriz N x N
for i in range(N):
    linha = []
    for j in range(N):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

soma = 0
quantidade = 0

# Percorre elementos acima da diagonal principal
for i in range(N): # Cada i representa uma linha da matriz
    for j in range(i + 1, N):  # Cada j representa uma coluna dessa linha, então só precisa ver quais são maiores que i (mostrar no quadro)
        soma += matriz[i][j]
        quantidade += 1

# Mostra o resultado com 1 casa decimal
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{soma / quantidade:.1f}")
