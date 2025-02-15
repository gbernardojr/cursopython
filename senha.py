# Montar um programa com um loop que fique 
# pedindo para digitar a senha correta até que 
# a pessoa digite a senha correta.

senha = "abcd1234"
senhaDigitada = ""

while senhaDigitada != senha:
    senhaDigitada = input("Digite a senha: ")
    if senhaDigitada != senha:
        print("Senha inválida")

print("Senha correta")