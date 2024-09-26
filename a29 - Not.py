#Operador lógico NOT
# Usado para inverte expressões
#not true = false
#not false =true

senha = input('Digite sua senha')
senha_correta = '12345'

if not senha:
    print("Voce não digitou nada")

elif senha == senha_correta:
    print('Voce entrou nos sistema')

else:
    print('Voce saui do sistema')