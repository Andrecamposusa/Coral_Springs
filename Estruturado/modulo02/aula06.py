# #importacao otimizada
from random import choice

nome1 = input("Digite seu nome>>> ")
nome2 = input("Digite seu nome>>> ")
nome3 = input("Digite seu nome>>> ")
nome4 = input("Digite seu nome>>> ")

#Variavel recebendo uma lista definida pela simbologia [],
lista = [   nome1,
            nome2,
            nome3, 
            nome4 
         ]

sorteado = choice(lista)

#print ultilizando polimorfismo e quebra de linhas
print( '='*20, 'NOME SORTEADO', '='*20 )

if sorteado == nome1:
    print("o nome sortado foi o primeiro digitado")
    print(f'o nome sorteado foi {sorteado}')

elif sorteado == nome2:
    print("o nome sortado foi o segundo digitado")
    print(f'o nome sorteado foi {sorteado}')

elif sorteado == nome3:
    print("o nome sortado foi o terceiro digitado")
    print(f'o nome sorteado foi {sorteado}')

elif sorteado == nome4:
    print("o nome sorteado foi o quarto digitado")
    print(f'o nome sorteado foi {sorteado}')
else:
    print("O seu sistema esta com erro")