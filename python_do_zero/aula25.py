'''
Formatção básica de strings
s - strinf
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''

# Utilizando f-strings

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:$>10}')
print(f'1000.4815156418145')
print(f'{1000.4815156418145:.1f}')
print(f'{1000.4815156418145:,.1f}')
print(f'{-1000.4815156418145:,.1f}')
print(f'{-1000.4815156418145:-,.1f}')
print(f'{1000.4815156418145:+,.1f}')
print(f'{1000.4815156418145:0=+10,.1f}')
print(f'O Hexadecimal de 1500 é {1500:08X}') 
print(f'{variavel!r}')