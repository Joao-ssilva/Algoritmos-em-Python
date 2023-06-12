from time import sleep
peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('PROCESSANDO...')
sleep(3)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está na faixa de ABAIXO DO PESO')
    #elif  <= 18.5 imc < 25:
elif  imc > 18.5 and imc < 25:
    print('PARABÉNS, Você está na faixa de PESSO NORMAL')
     #elif <= 25 imc < 30:
elif imc > 25 and imc < 30:
    print('Você está na faixa de SOBREPESO')
    #elif <= 30 imc < 40:
elif imc > 30 and imc < 40:
    print('Você está na faixa de OBESIDADE')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA. CUIDADO!')
