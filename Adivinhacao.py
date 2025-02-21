import random

print("**************************************************" "\n"
      "JOGO DE ADIVINHAÇÃO" "\n" "**************************************************")

escolhido = random.randint(1, 100)
rodada = 3
round = 1

while (round <= rodada):
        try:
            print("Tentativa {} de {}".format(round, rodada))

            tentativa = int(input("Digite o seu número da sorte (1 a 100): "))

            if tentativa == 0:
                print("acabou!")
                break

            if tentativa < 1 or tentativa > 100:
                print("Número inválido! Digite um número entre 1 e 100.")
                continue

            if tentativa == escolhido:
                print("🎉 Parabéns! Você acertou!")
                break
            else:

                if(tentativa > escolhido):
                    print("Errou, seu numero é menor doque esse")
                else:
                    print("Errou, seu numero é maior doque esse")

            round = round +1

        except ValueError:
            print("Digite um número válido!")


