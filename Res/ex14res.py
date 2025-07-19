"""Uma matriz quadrada é considerada um quadrado mágico se a soma 
dos elementos de cada linha, de cada coluna e das duas diagonais forem iguais. 
Implemente um algoritmo que leia uma matriz quadrada de ordem N x N (onde 
N <= 10 e determine se ela é um quadrado mágico e depois exibir 
Uma mensagem indicando se a matriz é ou não um quadrado mágico."""

def soma(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def eh_quadrado_magico(matriz):
    n = len(matriz)
    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0

    for i in range(n):
        soma_diagonal_principal += matriz[i][i]
        soma_diagonal_secundaria += matriz[i][n - 1 - i]

    # Verifica se as diagonais têm a mesma soma
    if soma_diagonal_principal != soma_diagonal_secundaria:
        return False

    # Verifica se todas as linhas e colunas têm a mesma soma
    for i in range(n):
        if soma(matriz[i]) != soma_diagonal_principal:
            return False
        coluna = [matriz[j][i] for j in range(n)]
        if soma(coluna) != soma_diagonal_principal:
            return False

    return True


# Exemplo de uso
matriz = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

if eh_quadrado_magico(matriz):
    print("\nA matriz é um quadrado mágico!")
else:
    print("\nA matriz NÃO é um quadrado mágico.")
