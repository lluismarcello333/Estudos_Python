'''
2. Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.:
   Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

horas = input('Que horas são, por favor? ')
horario = int(horas)

if horario >= 0 and horario <= 11:
    print('Bom dia!')
elif horario >= 12 and horario <= 17:
    print('Boa tarde!')
elif horario >= 18 and horario <= 23:
    print('Boa noite!')