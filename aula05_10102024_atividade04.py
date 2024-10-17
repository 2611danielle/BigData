# 4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada.
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser encarado como “Importado”;

def determinar_regiao(codigo):
    # Tabela de códigos e suas regiões
    tabela = {
        '1': 'Sul',
        '2': 'Sudeste',
        '3': 'Centro-Oeste',
        '4': 'Nordeste',
        '5': 'Norte'
    }
    
    # Retorna a região ou "Importado" se o código não estiver na tabela
    return tabela.get(codigo, 'Importado')

def main():
    # Leitura do código de origem
    codigo = input("Digite o código de origem do produto: ")

    # Determinação da região
    regiao = determinar_regiao(codigo)

    # Resultado
    print(f"A região de procedência do produto é: {regiao}")

if __name__ == "__main__":
    main()
