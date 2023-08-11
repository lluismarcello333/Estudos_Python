# conversão de tipos, coerção
# type convertion, typecasting, coercion é o ato de converter um tipo em outros tipos imutáveis e primitivos: 
# str, int, float, bool

# Em linguagens dinâmincas podemos passar dois números que a linguagem saberá como interpretar os dados
# Nos exemplos abaixo podemos ver exemplos de possíveis erros

#print('1' + 1) # Erro: Não é possível concatenar uma 'str' com um 'int'
print('a' + 'b') # Resultado 'ab'

# A concatenação é a operação que une duas ou mais strings em uma única string. 
# Em Python, a concatenação de strings é feita usando o operador de adição (+) ou o método join().

print(int('1'), type(int('1'))) # Dessa forma, podemos converter o tipo
print(int('1') + 1) # Assim, ao realizar essa operação, teremos o resultado '2'.
print(float('1') + 1) # Retorna um número float. Pois as somas de números in com float, retorna um número float.
print(bool('')) # Por padrão uma string vazia é considerada false. 
print(str(11) + 'b') # Retorna como resultado '11b'.