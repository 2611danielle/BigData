# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

#variáveis simples - são as que calculam a entrada de dados
# Entrada de dados
potencia_lampada = float(input("Digite a potência da lâmpada utilizada (em watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# Potência necessária por metro quadrado
potencia_por_m2 = 3  # watts

#variáveis para o cálculo de área e de potência
# Área do cômodo
area = largura * comprimento
# Potência total necessária
potencia_total_necessaria = area * 3 #3 watts por metro quadrado

#variáveis para o cálculo do número de lâmpadas e de bocais
# Número de lâmpadas necessárias
num_lampadas = potencia_total_necessaria / potencia_lampada
# Cada 3 m² tem um bocal para uma lâmpada
bocais = int(area / 3)

#exibição dos resultados (quaisquer das formatações são válidas)
# Saída de dados
print(f"Número de lâmpadas necessárias: {num_lampadas}")
print(f"Número de bocais disponíveis: {bocais}")





