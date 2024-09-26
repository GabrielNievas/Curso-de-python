#exercicio: utilizando os operadores de relacionais, peça dos valores e mostre primerio o maior e o menor depois

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O número {primeiro_valor} é maior que o numero {segundo_valor}')
elif segundo_valor > primeiro_valor :
    print(f'O número {segundo_valor} é maior que o numero {primeiro_valor}')
else:
    print(f'Os dois valores são iguais a {primeiro_valor}')

print('Obrigado e até logo !!!!')