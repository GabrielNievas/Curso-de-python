#Como formatar uma linha: Introduão a formatação de strings print(formato)

#Fstrings -> usar variáveis dentro de texto
#cuculadora de IMC
nome= "Gabriel da Silva Nievas"
altura = 1.78
peso = 77
imc = peso/altura**2

#fstring
linha1 = f'{nome} tem {altura:.2f} metros de altura, pesa {peso} kg e tem um IMC de {imc:.3f}'

print(imc)
print('O paciente', nome, 'tem', altura, "metros de altura, um peso de", peso, 'kilogramas e um IMC de:',imc,)
print(linha1)