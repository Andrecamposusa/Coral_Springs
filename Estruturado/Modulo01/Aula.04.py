nome = str(input('digite o seu nome :>'))
sobrenome = input('digite o seu sobrenome :>')
idade = int(input('digite sua idade :>'))

#print('o nome digitado foi ', nome,'o sobrenome digitado foi ', sobrenome,'a idade digitada foi ', idade) concatenacao
#print(f'o nome digitado foi {nome} o nome digitado foi {sobrenome} a idade digitada foi {idade}') interpolacao
print('o nome digitado foi {} o sobrenome digitado foi {} a idade digitada foi {}'.format(nome,sobrenome,idade))