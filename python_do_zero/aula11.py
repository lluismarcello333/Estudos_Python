# Precedencia de operadores: Significa que algumas coisas serão executadas antes de outras. Segue abaixo a ordem.
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
#Exemplo:
conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)
conta_2 = (1 + 1) ** (5 + 5) # 1024
print(conta_2)
conta_3 = (1 + (0.5 + 0.5)) ** 5 + 5 # 37.0
print(conta_3)
conta_4 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 37.0
print(conta_4)
