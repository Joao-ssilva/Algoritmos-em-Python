'''
Faça um programa  que jogue par ou ímpar com o computador. O jogo so será 
interrompido quando o jogador PERDER, mostrando o total de vitórias
consecultivas que ele conquistou no final do jogo
'''
from random import randint
print('=-' *30)
print('VAMOS JOGAAR PAR OU IMPAR')
print('=-'*30)
v = 0
p = ' '
while True:
    computador = randint(0,10)
    jogador = int(input('Diga um valor:'))
    soma = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar ? [P/I]')) .upper() .strip() [0]     
    print(f'Você jogou {jogador} e o computador {computador} a soma deu {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU')
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [N/S]')) .upper() .strip() [0]
    if continuar == 'S':
        print('Então vamos continuar.')
    else:
        break
print(f'GAME OVER! você venceu {v}')