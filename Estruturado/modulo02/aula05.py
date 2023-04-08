#importando modulo todo
import random

nome1 = input("Digite seu nome>>> ")
nome2 = input("Digite seu nome>>> ")
nome3 = input("Digite seu nome>>> ")
nome4 = input("Digite seu nome>>> ")
nome5 = input("Digite seu nome>>> ")

#Variavel recebendo uma lista definida pela simbologia [],
lista = [   nome1,
            nome2,
            nome3, 
            nome4, 
            nome5]

random.shuffle(lista)

polimorfismo = '*'*20

print(polimorfismo, 'CABECALHO do sorteio' , polimorfismo)
print(lista)