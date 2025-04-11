import random

print("**************************************************")
print("               JOGO DA FORCA")
print("**************************************************")

def carregar_palavra_secreta():
    try:
        with open("palavras.txt", "r") as arquivo:
            palavras = [linha.strip().upper() for linha in arquivo if linha.strip()]
        return random.choice(palavras)
    except FileNotFoundError:
        print("Arquivo 'palavras.txt' não encontrado.")
        exit()

def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros >= 1:
        print(" |      (_)   ")
    else:
        print(" |            ")

    if erros == 2:
        print(" |      \\     ")
    elif erros == 3:
        print(" |      \\|    ")
    elif erros >= 4:
        print(" |      \\|/   ")
    else:
        print(" |            ")

    if erros >= 5:
        print(" |       |    ")
    else:
        print(" |            ")

    if erros == 6:
        print(" |      /     ")
    elif erros >= 7:
        print(" |      / \\   ")
    else:
        print(" |            ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    palavra = carregar_palavra_secreta()
    letras_acertadas = ["_" for _ in palavra]
    letras_erradas = []
    erros = 0

    while erros < 7 and "_" in letras_acertadas:
        try:
            print("\nPalavra:", " ".join(letras_acertadas))
            chute = input("Digite uma letra: ").strip().upper()

            if chute == "0":
                print("Jogo encerrado!")
                break

            if len(chute) != 1 or not chute.isalpha():
                print("Digite apenas UMA letra válida.")
                continue

            if chute in letras_acertadas or chute in letras_erradas:
                print("Você já tentou essa letra.")
                continue

            if chute in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == chute:
                        letras_acertadas[i] = chute
            else:
                erros += 1
                letras_erradas.append(chute)
                print(f"Letra incorreta. Você tem {7 - erros} tentativas restantes.")
                desenhar_forca(erros)

        except Exception as e:
            print("Erro inesperado:", e)

    if "_" not in letras_acertadas:
        print("\nParabéns! Você acertou a palavra:", palavra)
    elif erros >= 7:
        print("\nVocê foi enforcado! A palavra era:", palavra)

    print("Fim do jogo!")

if __name__ == "__main__":
    jogar()
