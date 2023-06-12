'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar.
- Se já passou o tempo do alistamento.
Seu programa também deverá amostrar o tempo que falta ou que passou do prazo.
'''


from datetime import date
atual = date.today().year
genero = str(input('Qual seu gênero: [ M ] para masculino e [ F ] para feminino:')).upper() .strip()
nasc = int(input('Ano de nascimento'))
idade = atual - nasc
if genero == 'F':
    print('mulheres estão isentas dessa obrigatoriedade!')
if idade == 18 and genero == 'M':
    print(f'Quem nasceu em {nasc} vai ter {idade} anos em {atual}')
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and genero == 'M':
    saldo = 18 - idade
    print(f'Quem nasceu em {nasc} vai ter {idade} anos em {atual}')
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18 and genero == 'M':
    saldo = idade - 18
    print(f'Quem nasceu em {nasc} vai ter  {idade} anos em {atual}')
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = atual - saldo 
    print(f'Seu alistamento foi em {ano}')