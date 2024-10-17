# 2) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    n = int(input("Quantas pessoas você deseja cadastrar? "))
    
    for i in range(n):
        print(f"\nPessoa {i + 1}:")
        peso = float(input("Digite o peso (em kg): "))
        altura = float(input("Digite a altura (em metros): "))
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"IMC: {imc:.2f} - Classificação: {classificacao}")

if __name__ == "__main__":
    main()
