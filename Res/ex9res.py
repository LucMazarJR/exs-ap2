"""Faça um programa que leia um número N e depois N números inteiros. 
Para cada número, verifique se ele é primo (ou seja, divisível apenas por 1 e por ele mesmo) 
e imprima uma mensagem dizendo se o número é primo ou não, no formato: 
"X eh primo" ou "X nao eh primo"."""

def eh_primo(x):
    if x < 2: # Teste pra verificar se é igual ou menor a 1
        return False
    for i in range(2, x): #Verifica dentre todos os numeros de 2 até ele se existe algum que divide ele
        if x % i == 0:
            return False
    return True

N = int(input("Digite o número de vezes que se deve testar os números: "))

for i in range(N):
    X = int(input(f"Num {i+1}: "))
    if eh_primo(X):
        print(f"{X} é primo")
    else:
        print(f"{X} não é primo")
