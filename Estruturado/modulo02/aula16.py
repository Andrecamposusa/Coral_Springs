from time import sleep
cond = "sim"

while cond == "sim":
    var = int(input("Digite um numero que possa ser incrementado em um>> "))
    
    soma = var +1

    print(f" O numero digitado pelo usuario foi {var} e o incremento é {soma}")
    cond = str(input("Deseja continuar?\n sim\n nao\n >>"))
sleep(4)
print("Voce Saiu da Aplicacao")