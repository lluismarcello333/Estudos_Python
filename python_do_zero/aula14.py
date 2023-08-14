# Formatação de strings com método Format

a = 'A'
b = 'B'
c = 1.1

# Se colocarmos um ponto no final de uma string, conseguiremos ver o que temos de acesso dentro dessa string. Isso caracteriza um Objeto. Um Objeto pode executar ações, que por sua vez são chamadas de Métodos.
# Método é uma função que “pertence” a um objeto instância. (Em Python, o termo método não é aplicado exclusivamente a instâncias de classes definidas pelo usuário: outros tipos de objetos também podem ter métodos. Por exemplo, listas possuem os métodos append, insert, remove, sort, entre outros.

string = 'a={0} b={1} c={2:.2f}' 
formato = string.format(a,b,c)

print(formato)

# Parametro nomeado é quando damos um nome na criação das funções
#Exemplo

ex = 'a={nome1} b={nome2} c={nome3:.2f}' 
forma = ex.format(nome1=a,nome2=b, nome3=c)

print(forma)

