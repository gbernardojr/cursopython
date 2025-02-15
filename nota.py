nota = float(input("digite uma nota: "))

if nota > 10:
    print("você digitou número inválido")
elif nota >= 5:
    print("Aprovada")
elif nota >= 3:
    print("Recuperação")

elif nota < 0:
    print("você digitou número inválido")
else:
    print("voce não digitou menor que 0 - e está Reprovada")
