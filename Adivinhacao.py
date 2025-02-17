import random

print("**************************************************" "\n"
      "JOGO DE ADIVINHAÇÃO" "\n" "**************************************************")

escolhido = random.randint(1, 100)
tentativa = input("Digite o seu numero da sorte!: ")

while tentativa > "100":
    print("Numeros somentes até 100")
    tentativa = input("Digite o seu numero da sorte!: ")

if tentativa == escolhido:
    print("Parabens! você acertou!")
else:
    print("Errou Babaca!")
