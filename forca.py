import random

def mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def jogar():
    mensagem_inicial()

    palavra_secreta = gera_palavra_secreta()

    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativa = 1

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            print(f"voce tem {tentativa} tentativas de 6")
            tentativa = tentativa + 1

        enforcou = tentativa == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Parabens voce acertou")
    else:
        print("Voce perdeu")


    print("Fim do jogo")

def gera_palavra_secreta():
    arquivo = open("ttt.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicia_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


if(__name__ == "__main__"):
    jogar()