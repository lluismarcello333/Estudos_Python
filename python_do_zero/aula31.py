'''
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
'''

v1 = 'a'
print(id(v1)) # assim conseguimos ver a identidade de um elemento na memória


condicao = False

if condicao:
    passou_no_if = True
    print('Faça algo')
else: 
    print('Não faça algo')


# print(passou_no_if)

# Esse bloco de código é ineficaz, pois uma vez que a variável condicao é classificada como False, o código dentro do if não é lido e dessa forma, a variável que está dentro do if não é criada. Esse código apresentaria erro.

# Uma outra forma de escrever esse código seria:

condicao = False
passou_no_if = None


if condicao:
    passou_no_if = True # Dessa forma, a variaável passou_no_if só passará a ter o valor True se passar dentro desse if.
    print('Faça algo')
else: 
    print('Não faça algo')


print(passou_no_if, passou_no_if is None)

