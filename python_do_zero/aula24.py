''' 
Interpolação básica de strings
s -string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
nome = 'Luiz'
preco = 1000.95897643
# Supondo que desejamos escrever essa variável dessa forma. Podemos utilzar a interpolação
# variavel = 'Luiz, o preço total foi R$1000.95'
variavel = '%s, o preço total foi R$%.2f' % (nome,preco) # Nesse caso, o tipo e a ordem importam.
print(variavel)

print('O Hexadecimal de %d é %04x' % (15, 15)) # Dessa forma podemos converter um número em hexadecimal. Como utilizamos o 'x' minúsculo, o Hexadecimal será minúsculo.
print('O Hexadecimal de %d é %04X' % (1500, 1500)) # Dessa forma podemos converter um número em hexadecimal. Como utilizamos o 'X' maiúsculo, o Hexadecimal será maiúsculo.
# É importante ressaltar que para adicionarmos '0' Zeros no número decimal, basta utilizar p %0 + o número de zeros que deseja + 'x' ou 'X'.