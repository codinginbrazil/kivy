# Redução significa aplicar uma função que recebe dois parâmetros, 
# nos dois primeiros elementos de uma sequência, 
# aplicar novamente a função usando como parâmetros o resultado do primeiro par e
# o terceiro elemento, seguindo assim até o final da sequência.
# 
#  O resultado final da redução é apenas um elemento.

# importing functools for reduce() 
import functools as ft

def fat(n):
    return(ft.reduce(lambda x, y: x * y, range(1, n+1)))

print(fat(5))