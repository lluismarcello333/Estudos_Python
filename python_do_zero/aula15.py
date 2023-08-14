# Função input

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
print(f'A soma dos números é: {numero_1 + numero_2}') # Nesse caso a soma funcionará como uma concateção, pois o tipo do input é um str

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
print(f'A soma dos números é: {numero_1 + numero_2}') # Fazendo a conversão dos tipos dos inputs, podemos visualizar o resultado esperado

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# Se usarmos esse forma para poder fazer uma checagem no código, caso o usuário insira uma letra no lugar de um número ou um número no lugar de uma letra, o código vai quebrar na linha "int_numero_1 = int(numero_1)". Dessa forma poderemos verificar na leitura do erro o lugar onde ocorreu o erro, pois poderíamos ver que o erro teria ocorrido antes da execução da soma. 

print(f'A soma dos números é: {numero_1 + numero_2}')