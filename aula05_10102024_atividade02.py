#  2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²;

def calcular_caixas_azulejos(comprimento, largura, altura):
    # Calcula a área das paredes
    area_parede1 = altura * comprimento  # duas paredes com essa dimensão
    area_parede2 = altura * largura       # duas paredes com essa dimensão
    area_total = 2 * (area_parede1 + area_parede2)

    # Cada caixa de azulejos cobre 1,5 m²
    area_por_caixa = 1.5
    quantidade_caixas = area_total / area_por_caixa

    return quantidade_caixas

def main():
    # Leitura das dimensões da cozinha
    comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
    largura = float(input("Digite a largura da cozinha (em metros): "))
    altura = float(input("Digite a altura da cozinha (em metros): "))

    # Cálculo da quantidade de caixas de azulejos
    caixas = calcular_caixas_azulejos(comprimento, largura, altura)

    # Resultado
    print(f"Você precisará de aproximadamente {caixas:.2f} caixas de azulejos.")

if __name__ == "__main__":
    main()
