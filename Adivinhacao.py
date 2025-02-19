import random

print("**************************************************" "\n"
      "JOGO DE ADIVINHAÇÃO" "\n" "**************************************************")

escolhido = random.randint(1, 100)

while True:
    try:
        tentativa = int(input("Digite o seu número da sorte (1 a 100): "))

        if tentativa == 0:
            print("acabou!")
            break

        if tentativa < 1 or tentativa > 100:
            print("Número inválido! Digite um número entre 1 e 100.")
            continue  # Volta para o início do loop

        if tentativa == escolhido:
            print("🎉 Parabéns! Você acertou!")
            break
        else:
            if(tentativa > escolhido):
                print("Errou, seu numero é menor doque esse")
            else:
                print("Errou, seu numero é maior doque esse")

    except ValueError:
        print("Digite um número válido!")
