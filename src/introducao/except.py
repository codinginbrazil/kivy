try:
    x = (1 / 0)
    print (x)
except ZeroDivisionError:
    print ('Erro ao tentar dividir por zero.')