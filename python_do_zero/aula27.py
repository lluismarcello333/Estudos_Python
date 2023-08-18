'''
Fatiamento de Strings
0123456789
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: a função len retorna a quantidade de caracteres da str
'''

variavel = 'Olá Mundo'
print(variavel[5])
print(variavel[-4])

# Podemos usar o fatiamento
print(variavel[4:])
print(variavel[4:8]) # Os dois pontos indica para o python que deve ser executado o fatiamento. 
print(variavel[0:5]) # O último número não é incluído.
print(variavel[3]) # O O espaço também conta como um caractere.

# Função len: Conta caracteres das strings que tiver
print(len(variavel[3])) 
print(len(variavel)) # Usa-se para checar o tamanho de determinada string

# :p = o passo significa que indicaremos de quantos em quantos caracteres o python irá pular. Por exemplo:
print(variavel[0:9:1])
print(variavel[0:9:2])
print(variavel[0:9:3])
print(variavel[0:9:4])
print(variavel[::-1])
print(variavel[-1:-10:-1])
