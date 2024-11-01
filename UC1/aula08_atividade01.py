#ATIVIDADES:
#1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.
def calcular_multa(peso_peixes):
    limite = 100
    valor_multa_por_quilo_excedente = 10  # Valor da multa por quilo excedente

    if peso_peixes > limite:
        quilos_excedentes = peso_peixes - limite
        multa = quilos_excedentes * valor_multa_por_quilo_excedente
        return multa
    else:
        return 0  # Sem multa

# Exemplo de uso:
peso = 120  # peso dos peixes
multa = calcular_multa(peso)

if multa > 0:
    print(f"A multa a ser paga é: R$ {multa:.2f}")
else:
    print("Não há multa a ser paga.")