# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressao
# Quando tiver que separar os nomes em Python, utilizamos o sistema snake_case. É devido ao fato de usarmos o _ 'underline' entre as palavras.

nome_completo = 'Luiz Marcelo'
soma_um_mais_um = 2 + 2

print(nome_completo) # Luiz Marcelo
print(soma_um_mais_um) # 4

# As variáveis são usadas para deixar o código mais legível.
#Exemplo:
print(int('1'), type(int('1'))) # Dessa forma, podemos converter o tipo

int_um = int('1')
print(int_um + int_um)

# Se tivéssemos que alterar o código em 25 lugares que utilizam a variável 'int_um', só precisaríamos alterar o valor da variável.

nome = 'Luiz'
idade = 30
maior_de_idade = idade >= 18

print('Nome:', nome)
print('idade:', idade)
print('É maior?', maior_de_idade)