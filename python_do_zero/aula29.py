'''
Introdução ao try/except
try : Tentar executar o código
except : ocorreu algum erro ao tentar executar
'''

numero = input('Vou dobrar o número que você digitar: ')
dobro = float(numero)*2

print(f' O dobro do número que você digitou foi: {dobro:.2f}')

# Poderiamos utilizar:
numero_str = input(
        'Vou dobrar o número que você digitar: '
)
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dibri de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é o número.')

# o if não evita erros, pois apenas checa a lógica
# Aplicando o Try / except

try: 
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dibri de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é o número.')    