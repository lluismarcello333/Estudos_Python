# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = Ttrue

# Exemplo:
senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
else:
    print('Senha incorreta')    

#Esse código poderia ser checado dessa forma
senha_teste = '123457'

if not senha:
    print('Senha incorreta.')

# -----------------
print(not True) # False
print(not True) # True