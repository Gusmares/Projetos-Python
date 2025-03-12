print("**************************************************" "\n"
      "JOGO DE ADIVINHAÇÃO" "\n" "**************************************************")

import random

numero_secreto = random.randint(1, 100)

pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

while True:
    try:
        nivel = int(input("Defina o nível: "))
        if nivel not in [1, 2, 3]:
            print("Escolha um nível válido: 1, 2 ou 3.")
            continue
        break
    except ValueError:
        print("Digite um número válido!")

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

round = 1

while round <= total_de_tentativas:
    try:
        print(f"Tentativa {round} de {total_de_tentativas}")
        tentativa = int(input("Digite o seu número da sorte (1 a 100): "))

        if tentativa == 0:
            print("Jogo encerrado!")
            break

        if tentativa < 1 or tentativa > 100:
            print("Número inválido! Digite um número entre 1 e 100.")
            continue

        if tentativa == numero_secreto:
            print(f" Parabéns! Você acertou e fez {pontos} pontos!")
            break
        else:
            if tentativa > numero_secreto:
                print("Você errou! O número secreto é menor.")
            else:
                print("Você errou! O número secreto é maior.")

            pontos_perdidos = abs(numero_secreto - tentativa)
            pontos -= pontos_perdidos

        round += 1

    except ValueError:
        print("Digite um número válido!")

print("Fim do jogo!")
