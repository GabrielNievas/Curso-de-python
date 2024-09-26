#Outra forma de formatar: Format      - 16/09/2024
a = 'A'
b = 'B'
c = 1.115673489723
formato = 'a={}, b={} e c={}'.format(a,b,c)
string = 'a={},b={} e c={:.3f}'
formato2 = string.format(a,b,c)
string2 = 'a={nome1},b={nome2} e c ={nome3}'
formato3 = string2.format(nome1=a,nome2=b,nome3=c)
string3= 'a={0} a ={1} b={2} c={1}'
formato4=string3.format(a,b,c)
#O que está dentro de format são os argumentos
#Os mesmos argumentos são puxados na hordem em que aparecem
#Para não precisar da ordem, utilize os indices: o que vem primeiro é o 0, depois o 1 e depois o 2, etc...
#outro método, é por nome: vc dá um nome para o argumento e tem que chamá-lo pelo nome. Nesse caso vc tem que nomear todos os argumentos
#Erro 'out of range': tem mais argumentos do que variaveis para ele serem encaixados
print(formato)
print(formato2)
print(formato3)
print(formato4)