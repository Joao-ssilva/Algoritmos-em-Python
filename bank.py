'''
Crie um programa que simule o funcionamento de um caixa eletrônico. no início, pergunte ao usuário qual será o valor a ser sacado (Número inteiro) e o programa vai informar quantos cédulas de cada valor serão entregues.
OBS: considere que o caixa possui células de R$50, R$20, R$10 e R$1.
'''
print('='*30)
print('{:^30}'.format('BANK CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$' ))
total = valor
ced = 50
tot_ced = 0
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'O total de {tot_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0 # ele da dentro do else; então vai funcionar a cada if ou elif acima
        if total == 0:
            break