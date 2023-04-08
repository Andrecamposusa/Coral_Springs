#criar uma variavel que solicite dados 
casa = input("Digite qualquer coisa:> ")


#execute um print com descritivo e atribua a casa uma funcao de espaco
print('O dado digitado é um espco?',  casa.isspace() ) 
print('O dado digitado é um numero?', casa.isnumeric())
print('O dado digitado é letra?', casa.isalpha())
print('O dado digitado é alfanumerico?', casa.isalnum())
