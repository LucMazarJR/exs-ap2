"""Escreva um programa em python que leia um array de 20 inteiros, calcule e imprima:
a. A moda dos elementos no array (elemento mais freqüente).
b. A mediana dos elementos no array (elemento central)
c. A média"""
# Entrada: leitura dos 20 números
numeros = []

for i in range(20):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Média
soma = 0
for num in numeros:
    soma += num
media = soma / len(numeros)

# Ordenação simples
numeros.sort()

# Mediana
meio = len(numeros) // 2
if len(numeros) % 2 == 0:
    mediana = (numeros[meio - 1] + numeros[meio]) / 2
else:
    mediana = numeros[meio]

# Moda (contagem manual)
moda = numeros[0]
max_frequencia = 0

for i in range(len(numeros)):
    frequencia = 0
    for j in range(len(numeros)):
        if numeros[i] == numeros[j]:
            frequencia += 1
    if frequencia > max_frequencia:
        max_frequencia = frequencia
        moda = numeros[i]

# Saída
print(f"\nMédia: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
