# Operadores in e not in
#Strings são iteráveis
# Significa que podemos navegar item por item de uma string
# M a r c e l o
# 0 1 2 3 4 5 6
# Também podemos consultar por índices negativos
#  M  a  r  c  e  l  o
# -7 -6 -5 -4 -3 -2 -1 
nome = 'Marcelo'
print(nome[2])
print(nome[-5])

# Podemos verificar se um item está dentro de uma string
nome_1 = 'Luiz'

print('z' in nome_1)
print('ui' in nome_1)

print('z' not in nome_1)
print('o' not in nome_1)


#---------------------------------
# Podemos pedir para o usuário digitar o seu nome e verifica o que deseja encontrar

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} Não está em {nome}.')