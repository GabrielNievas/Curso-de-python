#operação condicionais: IF, Elif e Else
#If = "se" -> algo vai acontecer se vc fizer algo
#Else = senão for o entrar, faça algo diferente -> algo vai acontecer se o 'If' for descumprido
#Else não fica sozinho, apenas o If pode existir sozinho
#Elif = 'se não se' -> Se o 'If' inicial não for executado, execute o Elif.
#Pode haver mais de um Elif
#Ao encontrar um bloco verdadeiro, ele vai executar o que tiver de ser executado e vai pular para fora dos blocos.

entrada = input('Voce quer entrar ou sair do sistetma? ')

if entrada == 'entrar':
    print('Voce entrou no sistema')
elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print('Didite entrar ou sair')