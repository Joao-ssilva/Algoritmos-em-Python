'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal 
- 3 para hexadecimal
'''
numero = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para a converção
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
convecao = int(input('Sua opção:'))
if convecao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif convecao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif convecao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção invalida. Tente novamente.')
