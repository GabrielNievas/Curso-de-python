#entendo o fluxo do interpretador: if, elif e else
#pode ter if de baixo de if

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False
nao_condicao = False

if condicao1:
    print('este e o codigo do if')
if condicao2:
    print('este e o codigo do 2')
if condicao3:
    print('este e o codigo do 3')
if condicao4:
    print('este e o codigo do 4')
else:
    print('Este e o false')

#ao encontrar um true, ele pula para o final dos blocos de If, elf e else