# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

def calcular_consumo(litros_gastos, distancia_percorrida):
    if litros_gastos == 0:
        return 0
    return distancia_percorrida / litros_gastos

def calcular_lucro(valor_total, litros_gastos, preco_combustivel):
    custo_combustivel = litros_gastos * preco_combustivel
    lucro = valor_total - custo_combustivel
    return lucro

def main():
    # Constante para o preço do combustível
    PRECO_COMBUSTIVEL = 4.87

    # Leitura das informações
    odometro_inicial = float(input("Digite a marcação do odômetro no início do dia (km): "))
    odometro_final = float(input("Digite a marcação do odômetro no final do dia (km): "))
    litros_gastos = float(input("Digite o número de litros de combustível gasto: "))
    valor_total = float(input("Digite o valor total recebido dos passageiros (R$): "))

    # Cálculo da distância percorrida
    distancia_percorrida = odometro_final - odometro_inicial

    # Cálculo da média do consumo em km/L
    consumo = calcular_consumo(litros_gastos, distancia_percorrida)

    # Cálculo do lucro líquido do dia
    lucro = calcular_lucro(valor_total, litros_gastos, PRECO_COMBUSTIVEL)

    # Resultado
    print(f"Média de consumo: {consumo:.2f} km/L")
    print(f"Lucro líquido do dia: R$ {lucro:.2f}")

if __name__ == "__main__":
    main()
