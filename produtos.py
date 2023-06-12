'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverár perguntar se o usuário vai continuar No final, mostre:
A) Qual é o total gasto na compra. 
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais bataro.
'''
menor = 0
cont = 0
prod_m_bara = 0 
maisd_mil = 0
tot_gasto = 0
nome_prod_menor = ' '
while True:
    print('-'*30)
    print(f'{"LOJA SUPER BARATÃO":=^40}')
    print('-'*30)
    produto = str(input('Nome do produto:'))
    cont += 1
    preco = int(input('Preço: R$'))
    tot_gasto += preco
    if preco >= 1000:
        maisd_mil += 1
    # if cont == 1 or preco < menor: # achando o menor ja achamos o nome do produto mais barato
    if cont == 1:
        menor = preco
        nome_prod_menor = produto
    else: # nao precisaria mais desse else.
        if preco < menor:
            menor = preco
            nome_prod_menor = produto
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]')).upper() .strip() [0]
    if sn == 'N':
        break
print(f'O total da compra foi R${tot_gasto:.2f}')
print(f'ao todo foram {cont} compras')
print(f'Temos {maisd_mil} produto custando mais de R$1000.00')
print(f'O produto mais barado foi {nome_prod_menor} que custa R${menor:.2f}')
