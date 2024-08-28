'''Fazer um programa que receba um valor n no teclado e determine o maior.
A condição de término do programa é quando o usuário digitar zero.'''

maior = None
menor = None

while True:
    numeros = float(input("Digite um número: "))
    
    if numeros == 0:
        break

    if maior is None or numeros > maior:
        maior = numeros

    elif menor is None or numeros < menor:
        menor = numeros

if maior is not None and menor is not None:
    print("o maior: ", maior)
