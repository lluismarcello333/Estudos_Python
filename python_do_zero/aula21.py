# Operadores Lógicos 
'''
and (e) or (ou) not (não)
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira. 
Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
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


if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: # Utilizando a expessão usando o 'or', uma das proposições precisam ser verdadeiras.
    print('Entrar')
else:
    print('Sair')


# É importante ressaltar que o código é executado de cima para baixo e da esquerda para a direita. Dessa forma, quando analisamos o caso abaixo, podemos notar que como o operador lógico que estamos utilizando é o 'or', quando ele encontrar qualquer valor que considere a expressão verdadeira, ele irá parar e nos retornar o resultado.
senha = False or False or 0 or 'abd' or True

print(senha)
print(False or True or 0 or 'abd')

# Outro exemplo:
senha_do_usuario = input('Senha: ') or 'Sem senha!'
print(senha_do_usuario)
