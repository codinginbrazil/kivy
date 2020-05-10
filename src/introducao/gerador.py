# Geradores
#
# As funções geralmente seguem o fluxo convencional de processar, 
# retornar valores e encerrar. 
# 
# Geradores funcionam de forma similar, 
# porém lembram o estado do processamento entre as chamadas, 
# permanecendo em memória e retornando o próximo item esperado quando ativados.
# 
# Os geradores apresentam várias vantagens em relação às funções convencionais:
#   * Lazy Evaluation: geradores só são processados quando é realmente
#     necessário, sendo assim, economizam recursos de processamento.
#   * Reduzem a necessidade da criação de listas.
#   * Permitem trabalhar com sequências ilimitadas de elementos.

# Existem vários geradores que fazem parte da própria linguagem, 
# como o builtin xrange() 22 . 
# Além disso, no módulo itertools, estão definidos vários geradores úteis.

#Gera números pares infinitamente...
def gen_pares():
    i = 0
    while True:
        i += 2
        yield i

for n in gen_pares():
    print(n)