#crie um código que seja capaz de ler e armazenar
#uma sequência de 20 números pares e 20 números ímpares.
#obs: utilize estruturas de repetição para fechar esse conjunto
#de números.

# Inicializa as listas para armazenar os números pares e ímpares
numeros_pares = []
numeros_impares = []

# Loop para coletar 20 números pares
while len(numeros_pares) < 20:
    numero = int(input("Digite um número par: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        print("O número não é par. Tente novamente.")

# Loop para coletar 20 números ímpares
while len(numeros_impares) < 20:
    numero = int(input("Digite um número ímpar: "))
    if numero % 2 != 0:
        numeros_impares.append(numero)
    else:
        print("O número não é ímpar. Tente novamente.")

# Exibe os resultados
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
