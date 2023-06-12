'''
Crie um programa que tenha uma tupla com várias palavras (Não usar acentos)
Depois disso, para cada palavra, quais são as suas vogais.
'''
lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO','GRATIS',
        'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMARDOR','FUTURO',)
for c in lista:
        print(f'\nNa palavra {c.upper()} temos:', end='') 
        for letra in c:
            if letra.lower() in 'aeiou':
                print(f'{letra}', end=' ')