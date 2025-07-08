"""Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e
um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escreva
um programa, que imprima o tempo necessário para que a população do país A ultrapasse
a população do país B."""

# População inicial
pop_a = 5000000
pop_b = 7000000

# Taxas de crescimento
taxa_a = 0.03  # 3%
taxa_b = 0.02  # 2%

anos = 0

# Enquanto A não ultrapassar B, continua crescendo
while pop_a <= pop_b: #Enquanto não ultrapassar / Enquanto pois não temos noção de quantas vezes ocorrera o laço até o evento acontecer
    #Ambos vão aumentar em passos diferentes, até um alcançar o outro
    pop_a += pop_a * taxa_a 
    pop_b += pop_b * taxa_b
    anos += 1

# Resultado
print(f"Serão necessários {anos} anos para que o país A ultrapasse o país B.")
