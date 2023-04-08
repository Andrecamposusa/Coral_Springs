n1 = float(input("Digite sua primeira nota>> "))
n2 = float(input("Digite sua segunda  nota>> "))

media = (n1 + n2) / 2

if media >= 7:
    print('parabens voce atingiu a media') 
    
elif media < 7:
    print("voce foi reprovado")