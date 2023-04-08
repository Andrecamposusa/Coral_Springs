
#importacao otimizada
from time import sleep

inicio = int(input("Digite o numero de inicio:>> "))
fim = int(input("Digite o numero de fim:>> "))
passo = int(input("Digite o numero de passo:>> "))

for c in range(inicio, fim, -passo):
    sleep(1)
    print(c)