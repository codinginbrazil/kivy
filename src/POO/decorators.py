# [PEP 318](https://www.python.org/dev/peps/pep-0318/)
#
# Decoradores (decorators) são funções que são aplicadas em outras funções e
# retornam funções modificadas. 
# Decoradores tanto podem ser usados para criar ou 
# alterar características das funções (que são objetos) quanto para “envolver” as funções, 
# acrescentando uma camada em torno delas com novas funcionalidades.
#
# https://pythonacademy.com.br/blog/domine-decorators-em-python

def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()