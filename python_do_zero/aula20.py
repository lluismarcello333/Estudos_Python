# Operadores Lógicos 
'''
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
são considerados falsos
- 0 
- 0.0 
- '' 
- False
Também existe o tipo None que é usado para representar um não valor.
'''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'


if entrada == 'E' and senha_digitada == senha_permitida: # Utilizando a expessão utilizando o 'and', as duas proposições precisam ser verdadeiras.
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
print(bool('')) # Será false 
print(bool(0)) # Será false
print(bool(0.0)) # Será false
print(bool(' ')) # Será true, pois já existe valor por causa do espaço