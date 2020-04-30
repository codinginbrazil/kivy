# importando o módulo string
import string

# Cria uma string template
template = string.Template('$aviso aconteceu em $quando')

# Preenche o modelo com um dicionário
mensagem = template.substitute({
    'aviso': 'Falta de eletricidade',
    'quando': '03 de Abril de 2020'
    })

# Falta de eletricidade aconteceu em 03 de Abril de 2002
print (mensagem)