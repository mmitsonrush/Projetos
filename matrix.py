import random

def jogar():

    print("*******************")
    print("bem vindo a Matrix!")
    print("*******************")

    senha_secreta = random.randrange(1,11)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nível de segurança da Matrix!")
    print("(1) Segurança facilitada (2) Segurança média (3) Segurança avançada")

    nivel = int(input("Digite o nível de segurança: "))

    if(nivel == 1):
        print("Você escolheu: Segurança facilitada")
        total_de_tentativas = 10
    elif(nivel == 2):
        print("Você escolheu: Segurança média")
        total_de_tentativas = 5
    else:
        print("Você escolheu: Segurança avançada")
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

        Senha = input("digite sua senha entre 1 e 10: ")
        print("Você digitou", Senha)
        Senha = int(Senha)

        if(Senha < 1 or Senha > 10):
            print("Você deve digitar um número entre 1 e 10!")
            continue

        acertou = Senha == senha_secreta
        maior = Senha > senha_secreta
        menor = Senha < senha_secreta

        if (acertou):
            print("Senha Correta! Acesso Liberado!")
            print("**********************")
            print("Você acessou a Matrix!")
            print("**********************")
            print("Sua pontuação é {}".format(pontos))
            break
        else:
            if (maior):
                print("Senha incorreta! Acesso Negado! A Senha que você colocou é MAIOR que a Senha Secreta!")
            elif (menor):
                print("Senha incorreta! Acesso Negado! A Senha que você colocou é MENOR que a Senha Secreta!")
            pontos_perdidos = abs(senha_secreta - Senha)
            pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()

