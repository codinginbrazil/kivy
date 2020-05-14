# Por conta de sua característica de serem objetos de primeira classe, 
# é possível definirmos funções dentro de outras funções. 
# Esse é o conceito de nested functions. 

def party():
    print("Estou de fora =[")

    def start_party():
        return "Estamos dentro! Uhullll!"

    def finish_party():
        return "A festa acabou! =["

    print(start_party())
    print(finish_party())

party()