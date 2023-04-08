#dicionario = { 'Nome':'Andre', 'sobrenome':'Granemann', 'idade':18}

nome = input("Digite seu nome>>> ")
sobrenome = input("Digite seu sobrenome>>> ")
idade = int(input("Digite sua idade>>> "))
altura = input("Digite sua altura>>> ")



pessoa = { 'Nome': nome,'Sobrenome': sobrenome,'Idade': idade,'Altura' : altura }


print(
      f'''A altura é de :{pessoa['Altura']}
e o nome é {pessoa['Nome']}
        '''
      )