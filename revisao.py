# Entrada
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
print('Qual operação você deseja? Digite ')
print("A - Adição")
print("S - Subtração")
print("M - Multiplicação")
print("D - Divisão")
print("E - Exponenciação")
operacao = input("Qual sua escolha? ")

# Processamento
resultado = 0
if (operacao.upper() == 'A'):
    resultado = numero1 + numero2
elif (operacao.upper() == 'S'):
    resultado = numero1 - numero2
elif (operacao.upper() == 'M'):
    resultado = numero1 * numero2
elif (operacao.upper() == 'D'):
    resultado = numero1 / numero2
elif (operacao.upper() == "E"):
    resultado = numero1 ** numero2
else:
    resultado = "Opção inválida."


# Saída
print("O resultado é: ",resultado)

