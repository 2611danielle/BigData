def verificar_valor(valor):
    if valor >= 0:
        return "O valor é positivo."
    else:
        return "O valor é negativo."

def main():
    # Leitura do valor
    valor = float(input("Digite um valor: "))

    # Verificação do valor
    resultado = verificar_valor(valor)

    # Resultado
    print(resultado)

if __name__ == "__main__":
    main()
