limite = 101
contador = 0
sair = False  # True ou False

while sair == False:
    print("Contando.: ", contador)
    contador += 1
    resposta = input("Desejar parar o contador? S/N: ")
    if resposta == "N":
        sair = False
    else:
        sair = True

print("Final da contagem")