from time import sleep

#1-parte do codigo que referencia as variaveis representando a pessoa
nome = str(input("Digite seu nome >> "))
sobrenome = str(input("Digite seu sobrenome>> "))
idade = int(input("Digite sua idade>> "))

#2-parte estrutura de repeticao 
# realizando uma media de notas baseado em uma lista
for lista in range(0, 2):

    nota = int(input("Digite sua nota>> "))

    lista_notas = [nota]

    media = sum(lista_notas) / len(lista_notas)


#3 parte
situacao = "Reprovado por favor tente novamente"


# 4 parte estrutura selecao
if media >= 7:
    sleep(2)

    for c in range(0, 10):
        print("*")
        sleep(1)
    situacao = "Parabens Voce foi aprovado no curso de python "


dicionario_alunos = {
                    'Nome':nome,
                    'SobreNome':sobrenome,
                    'idade':idade,
                    'Media': media,
                    'Situacao': situacao
                      }

#print(dicionario_alunos)
print(f"{dicionario_alunos['Nome']} {dicionario_alunos['SobreNome']} {dicionario_alunos['idade']} {dicionario_alunos['Media']} {dicionario_alunos['Situacao']}")