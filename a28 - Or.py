# operador lógico 'OR'
#Qualquer experessão verdadeira avalia a expressão inteira com verdadeira


entrada = input('[E]ntrar o [S]air: ')
senha_permitida = '4567'
senha_perguntada =input('Digite a senha: ')

if (entrada == 'E' or entrada == 'e') and senha_permitida == senha_perguntada:
    print('Voce entrou no sistema')
# No caso, foi utilizado os parenteses para que o "or possa ser avaliado primeiro que o and"
else:
    print('Voce não entrou no sistema')


variavel_de_teste = False or 0 or 0.0 or 'ola'
print(variavel_de_teste)
print(variavel_de_teste == True)