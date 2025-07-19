"""Dada uma matriz de dimensões N x M, escreva um programa que imprima seus 
elementos em ordem espiral, começando  pelo canto superior esquerdo e seguindo 
no sentido horário até que todos os elementos tenham sido percorridos."""

def leitura_espiral(matriz):
    linha_inicio = 0
    linha_fim = len(matriz) - 1
    coluna_inicio = 0
    coluna_fim = len(matriz[0]) - 1

    resultado = []

    while linha_inicio <= linha_fim and coluna_inicio <= coluna_fim:
        # Percorre a linha superior da esquerda para a direita
        for col in range(coluna_inicio, coluna_fim + 1):
            resultado.append(matriz[linha_inicio][col])
        linha_inicio += 1

        # Percorre a coluna direita de cima para baixo
        for lin in range(linha_inicio, linha_fim + 1):
            resultado.append(matriz[lin][coluna_fim])
        coluna_fim -= 1

        # Percorre a linha inferior da direita para a esquerda (se ainda houver)
        if linha_inicio <= linha_fim:
            for col in range(coluna_fim, coluna_inicio - 1, -1):
                resultado.append(matriz[linha_fim][col])
            linha_fim -= 1

        # Percorre a coluna esquerda de baixo para cima (se ainda houver)
        if coluna_inicio <= coluna_fim:
            for lin in range(linha_fim, linha_inicio - 1, -1):
                resultado.append(matriz[lin][coluna_inicio])
            coluna_inicio += 1

    return resultado

# Exemplo de uso:
matriz = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]

espiral = leitura_espiral(matriz)
print("Leitura em espiral:")
print(espiral)
