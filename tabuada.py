'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado o programa será 
interrompido quando o número solicitado for negativo  
'''

while True:
    n1 = int(input('Quer ver a tabuada de qual valor?'))
    if n1 < 0:
        break
    print('-='*30)
    for c in range(1,10+1):
        mult = n1 * c
        print(f'{n1} x {c:2} = {mult}')
    print('-='*30)
print('PROGRAMA TABUADA ENCERRADO. volte sempre!')