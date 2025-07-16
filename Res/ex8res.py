"""
Leia uma matriz 5x10 que se refere às respostas de 10 questões de múltipla escolha, referentes a 5 alunos.
Leia também um vetor de 10 posições contendo o gabarito de respostas (as alternativas podem ser 'a', 'b', 'c' ou 'd').
Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado, 
contendo a pontuação (quantidade de acertos) correspondente a cada aluno.
"""

# Leitura da matriz de respostas (5 alunos x 10 questões)
respostas = []
for i in range(5):
    # Cada aluno representa uma linha, e as colunas de cada linha as respostas das questões
    aluno = []
    print(f"\nAluno {i+1}:")
    for j in range(10):
        resp = input(f"Resposta da questão {j+1} (a/b/c/d): ").lower()
        aluno.append(resp)
    respostas.append(aluno)

# Leitura do gabarito
print("\nInforme o gabarito:")
gabarito = []
for j in range(10):
    gabarito.append(input(f"Gabarito da questão {j+1} (a/b/c/d): ").lower())

# Comparação e cálculo dos resultados
resultado = [] # Vetor que vai guardar os 5 resultados
for i in range(5):
    acertos = 0
    for j in range(10):
        if respostas[i][j] == gabarito[j]:
            acertos += 1
    resultado.append(acertos)

# Exibição dos resultados
print("\nResultado (pontuação de cada aluno):")
for i, pontos in enumerate(resultado):
    print(f"Aluno {i+1}: {pontos} acertos")
