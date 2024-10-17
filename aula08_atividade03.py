# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.
# Cardápio do restaurante
cardapio = {
    "1": {"nome": "Açaí", "preco": 20.00},
    "2": {"nome": "Foccacia", "preco": 10.00},
    "3": {"nome": "Homus", "preco": 20.00},
    "4": {"nome": "Salada de fradinho", "preco": 25.00}
}

# Função para exibir o cardápio
def exibir_cardapio():
    print("Cardápio do Restaurante:")
    for chave, item in cardapio.items():
        print(f"{chave}. {item['nome']} - R$ {item['preco']:.2f}")

# Função para realizar um pedido
def realizar_pedido():
    total = 0
    while True:
        exibir_cardapio()
        escolha = input("Escolha o número do item que deseja pedir (ou 's' para sair): ")
        if escolha.lower() == 's':
            break
        if escolha in cardapio:
            total += cardapio[escolha]['preco']
            print(f"Você adicionou {cardapio[escolha]['nome']} ao seu pedido.")
        else:
            print("Opção inválida. Tente novamente.")
    return total

# Função para fechar a conta
def fechar_conta(total):
    print(f"Total da conta: R$ {total:.2f}")
    pagamento = float(input("Digite o valor que você está pagando: R$ "))
    if pagamento >= total:
        troco = pagamento - total
        print(f"Pagamento aceito. Seu troco é R$ {troco:.2f}. Obrigado e até a próxima!")
    else:
        print("Valor insuficiente. Tente novamente.")

# Função principal para executar o sistema
def main():
    total = realizar_pedido()
    if total > 0:
        fechar_conta(total)

# Iniciar o sistema
if __name__ == "__main__":
    main()
