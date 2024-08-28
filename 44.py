'''Receber um número e verificar se está entre 100 e 200. Se estiver na
faixa, imprimir: "Você digitou um número entre 100 e 200", senão estiver
na faixa, imprimir: "Você digitou um número fora da faixa entre100 e 200".'''

num = float(input('Digite um número entre 100 e 200: '))

if 100 <= num <= 200:
    print("Você digitou um número entre 100 e 200.")
else:
    print("Você digitou um número fora da faixa entre100 e 200.")