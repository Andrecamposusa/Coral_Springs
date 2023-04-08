#variavel recebendo o tipo primitivo string
#Tudo que esta entre aspas é a representatividade de um texto
nome = "andre"

#variavel recendo apenas numeros é a representacao do tipo primitivo int
#diferente da string voce nao precisa colocar aspas
#pois o python por ser dinamico ele é auto interpretativo
idade = 15

#variavel salario recebe numeros com casas decimais que representam o tipo primitivo floate
#diferente do inte ele nessesita de mais processamento para execucao
salario = 1.200

#duas variaveis representando o tipo primitivo booleano
# este tipo primitivo faz uma validacao de verdadeiro ou falso para os dados
verdadeira = True
falso = False

n1 = float(input("Digite o primeiro salario:> "))

n2 = float(input("Digite o segundo salario:> "))

print("o primeiro salario foi {}\no segundo salario foi {}\n".format(n1, n2))