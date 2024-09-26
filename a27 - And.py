#Operador lógico 'AND'
#todas as condições temque ser verdadeiras, ou no caso true
#Se uma parte da expressão for False, a expressão inteira será negativa
#No caso, Uma expressão será negativa quando confrontada com um valor boolean
#Valores falsos : '0' , '0.0' e '' .

entrada = input('[E]ntrar o [S]air: ')
senha_permitida = '4567'
senha_perguntada =input('Digite a senha: ')

if entrada == 'E' and senha_permitida == senha_perguntada:
    print('Voce entrou no sistema')

else:
    print('Voce não entrou no sistema')
print(f'{senha_perguntada == senha_permitida} Primeiro print')

print(True and False and True)
print(bool(0))
# Perceba na linha 18 que dentro do "print(True and False and True)" tem um false entre os " and's "
#nesse caso, o interpretador nem irá checar o segundo and, pois antes dele já tem um false. No caso,
#o inerpretador vai para no false e vai considerar a expressão inteira como sendo falsa.
#o interpretador avalia a expressão inteira naquele valor ngativo