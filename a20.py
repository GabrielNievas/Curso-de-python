#Função para coletar dados dos usuarios
#input()
#input("Qual o seu nome?")

nome = input('Qual o seu nome?')
print(f'o se nome é {nome}')
#o que for digitado logo apos o" Qual o seu nome", será alocado na variavel'nome'
#a alocação faz com que o dado se torne tipo string
numero1 = input('Digite um numero:')
numero2 = input('Digite um numero:')
print(f'A concatenação dos numeros é: {numero1 + numero2}')
#É necessário fazer a mudança do tipo de variavel para que uma soma possa ser feita
intnumero1 = int(numero1)
intnumero2 = int(numero2)
print(f'A soma dos numeros é: {intnumero1 + intnumero2}')