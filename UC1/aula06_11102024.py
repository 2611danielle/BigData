### ESTRUTURAS DE REPETIÇÃO ###
# FOR: sabemos a quantidade de vezes que o laço de repetição foi executado.

#for i in range(5):
    #numero=int(input('Digite um número:'))
    #print(f'Dobro:{numero*2}')

# WHILE: queremos a repetição quando a condição for verdadeira.
    
# Exemplo1:
#contador=0
#while True:
    #numero=int(input('Digite um número:'))
    #print(f'Triplo:{numero*3}')
    #contador=contador+1

# Exemplo2:
#num=5
#while num<3:
    #print('teste')
      

# DO WHILE: similar ao "WHILE", mas garante o bloco seja lido ao menos 1 vez
    #antes da verificação da condição.
 #break #continue #pass

#num=5
#while True:
    #print('teste')
    #if not(num<3):
        #break
    
#ATIVIDADE DE FIXAÇÃO:

#>>>Desenvolva um programa que guarde os dados de 10 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos 
#menores de 18 anos não podem participar. Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica e a 
#experiência profissional.

'''from datetime import datetime

def calcular_idade(data_nascimento):
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.now()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

def coletar_dados():
    candidatos = []
    
    while len(candidatos) < 10:
        print(f"\nCandidato {len(candidatos) + 1}:")
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        
        if calcular_idade(data_nascimento) < 18:
            print("Candidato menor de 18 anos não pode se candidatar.")
            continue
        
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        formacao = input("Formação Acadêmica: ")
        experiencia = input("Experiência Profissional: ")
        
        candidato = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "telefone": telefone,
            "email": email,
            "formacao": formacao,
            "experiencia": experiencia
        }
        
        candidatos.append(candidato)
        print("Candidato cadastrado com sucesso!")
    
    return candidatos

def mostrar_candidatos(candidatos):
    print("\nCandidatos Cadastrados:")
    for i, candidato in enumerate(candidatos):
        print(f"\nCandidato {i + 1}:")
        for chave, valor in candidato.items():
            print(f"{chave.capitalize()}: {valor}")

def main():
    candidatos = coletar_dados()
    mostrar_candidatos(candidatos)

if __name__ == "__main__":
    main()'''



# ESTRUTURAS DE ARMAZENAMENTO
    
# LISTAS 'conversão:list()'
candidatos=[] #lista vazia
lista1=[2,4,6,8,10]
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[4])
print(lista1[-1])
print(lista1[-2])
lista1.append(20)
lista1.insert(26,3)
lista1.insert(2,33)
print(lista1)
print(len(lista1))



# TUPLAS 'conversão:tuple()'
senhas=() #tupla vazia


# DICIONÁRIOS 'conversão:dict()'
estados_uf{} #dicionário vazio