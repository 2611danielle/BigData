#ATIVIDADE: (github)

#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.

class NumeroImparError(Exception):
    """Exceção personalizada para números ímpares."""
    pass

def obter_par_de_numeros():
    while True:
        try:
            entrada = input("Digite um par de números inteiros (separados por espaço): ")
            num1, num2 = map(int, entrada.split())
            
            if num1 % 2 != 0 or num2 % 2 != 0:
                raise NumeroImparError("Um dos números é ímpar. Por favor, insira apenas números pares.")
            
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, insira dois números inteiros.")
        except NumeroImparError as e:
            print(e)
        finally:
            print("Operação finalizada.")

def main():
    for i in range(3):
        print(f"\nPar {i + 1}:")
        num1, num2 = obter_par_de_numeros()
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} é {soma}.")

if __name__ == "__main__":
    main()
