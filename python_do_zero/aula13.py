# Formatação de Strings


nome = 'Luiz Marcelo'
altura = 1.80
peso = 95
imc = peso / (altura ** 2)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc )

#f-strinhgs
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)

#Outra de forma de formatar é usando a função Format que veremos mais a frente.
