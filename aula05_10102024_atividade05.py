# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

def calcular_media(nota1, nota2, nota_optativa):
    # Se a nota optativa for -1, não a consideramos
    if nota_optativa == -1:
        return (nota1 + nota2) / 2

    # Identifica a nota mais baixa
    nota_baixa = min(nota1, nota2)
    
    # Substitui a nota mais baixa pela nota optativa
    if nota_baixa == nota1:
        media = (nota_optativa + nota2) / 2
    else:
        media = (nota1 + nota_optativa) / 2

    return media

def classificar_aluno(media):
    if media >= 6.0:
        return "Aprovado"
    elif media < 3.0:
        return "Reprovado"
    else:
        return "Exame"

def main():
    # Leitura das notas
    nota1 = float(input("Digite a nota da primeira avaliação: "))
    nota2 = float(input("Digite a nota da segunda avaliação: "))
    nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

    # Cálculo da média
    media = calcular_media(nota1, nota2, nota_optativa)

    # Classificação do aluno
    resultado = classificar_aluno(media)

    # Resultado
    print(f"Média do semestre: {media:.2f}")
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
