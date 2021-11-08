from random import randint


class Cores:
    verde = '\033[1;32m'
    vermelho = '\033[1;33m'
    fim = '\033[0m'


def boasvindas():
    print(Cores.verde + '-' * 35 + Cores.fim)
    print('        Bem vindo(a) ao:')
    print(Cores.vermelho + '      JOGO DA ADIVINHAÇÃO!' + Cores.fim)
    print('Vou pensar em um número de 1 a 100')
    print('       Dê o seu chute!!!')
    print(Cores.verde + '-' * 35 + Cores.fim)


def variaveisderespostamaior():
    if tentativas >= 2 and tentativas < 4:
        print('Errou de novo. Dessa vez escolha um número maior.')
    elif tentativas >= 4 and tentativas < 7 :
        print(f'É maior que {chute}. Vamos ficar aqui até amanhã.')
    elif tentativas >= 7:
        print('ZZZZZZZZZ... Maior')
    else:
        print('Você errou. Eu pensei em um número maior. Tente novamente')


def variaveisderespostamenor():
    if  tentativas >= 2 and tentativas <4:
        print('Errou de novo. Dessa vez escolha um número menor.')
    elif tentativas >= 4 and tentativas < 7:
        print('Errrrouuu. É menor.')
    elif tentativas >= 7:
        print('ZZZZZZZZZ... Menor')
    else:
        print('Você errou. Eu pensei em um número menor. Tente novamente')


num_gerado = randint(1, 101)
tentativas = 1

boasvindas()

while True:
    try:
        chute = int(input('Chute um número: '))
        if chute > 100 or chute < 1:
            print('Digite um número entre 1 e 100.')
        else:
            if chute < num_gerado:
                variaveisderespostamaior()

            elif chute > num_gerado:
                variaveisderespostamenor()

            elif chute == num_gerado:
                if tentativas >= 8:
                    print(f'PARABÉNS. Você acertou com "APENAS" {tentativas} tentativas.')
                else:
                    print(f'PARABÉNS. Você acertou com {tentativas} tentativas.')
                opcao = input('Quer jogar novamente? [s/n]').upper()

                if opcao in "N":
                    print('\nObrigado por jogar. Até a próxima!')
                    break
                else:
                    print("\n" * 130)
                    tentativas = 0
            tentativas += 1
    except ValueError:
        print('Digite um número inteiro!')
