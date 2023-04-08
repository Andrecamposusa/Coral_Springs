#Operadores relacionais
# validador
validador = True
idade = int(input('Digite sua idade>>> '))


#expressão da igualdade
validador = (idade == 18)
print(validador)

#expressão da diferença
validador = ( idade != 18 )
print(validador)

#--- Criação de variável booleana através de expressão da menor
validador = ( idade < 18 )
print(validador)

validador = ( idade > 18 )
print(validador)

#--- Criação de variável booleana através de expressão da maior e igual
validador = ( idade >= 18 )
print(validador)

#--- Criação de variável booleana através de expressão da menor e igual
validador = ( idade <= 18 )
print(validador)