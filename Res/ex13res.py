"""Leia uma matriz de inteiros e substitua todas as linhas e colunas que 
contêm pelo menos um zero por zeros. A modificação deve ser feita diretamente 
na matriz fornecida (in-place), sem o uso de estruturas auxiliares.”"""

def zera_matrix(mat):
    n = len(mat)
    m = len(mat[0]) if n > 0 else 0

    linhas_com_zero = [False] * n
    colunas_com_zero = [False] * m

    # 1ª passagem: identificar linhas e colunas com zero
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                linhas_com_zero[i] = True
                colunas_com_zero[j] = True

    # 2ª passagem: aplicar zeros nas linhas/colunas marcadas
    for i in range(n):
        for j in range(m):
            if linhas_com_zero[i] or colunas_com_zero[j]: # Se sua coluna ou linha possuirem um zero então vai transformar 
                mat[i][j] = 0

# Exemplo de uso:
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    zera_matrix(mat)
    for linha in mat:
        print(linha)
    # Saída esperada:
    # [1, 0, 3]
    # [0, 0, 0]
    # [7, 0, 9]
