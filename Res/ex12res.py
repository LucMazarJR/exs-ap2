"""Verificar se uma matriz dada forma um Quadrado Latino de ordem N, no qual
em cada linha e em cada coluna aparecem todos os inteiros 1,2,3, ... N, ou seja, cada linha
ou coluna é permutação dos N primeiros números inteiros. """

def eh_quadrado_latino(matriz):
    N = len(matriz)

    # Verifica cada linha
    for i, linha in enumerate(matriz):
        contagem = [0]
        for c in range(N):
            contagem.append(0)  # Criamos a lista [0, 0, ..., 0] com N+1 elementos

        for numero in linha:
            if numero < 1 or numero > N:
                print(f"Número fora do intervalo na linha {i + 1}: {numero}")
                return False
            contagem[numero] += 1

        # Verifica se cada número apareceu exatamente 1 vez
        if contagem[1:] != [1] * N:
            print(f"Linha {i + 1} inválida: {linha}")
            return False

    # Verifica cada coluna
    for j in range(N):
        contagem = [0]
        for c in range(N):
            contagem.append(0)

        for i in range(N):
            numero = matriz[i][j]
            if numero < 1 or numero > N:
                print(f"Número fora do intervalo na coluna {j + 1}: {numero}")
                return False
            contagem[numero] += 1

        if contagem[1:] != [1] * N:
            print(f"Coluna {j + 1} inválida")
            return False

    return True

N = 3
matriz = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]

if eh_quadrado_latino(matriz):
    print("A matriz É um quadrado latino.")
else:
    print("A matriz NÃO é um quadrado latino.")
