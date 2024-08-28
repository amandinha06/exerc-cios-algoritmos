'''Elaborar um programa que efetue a leitura de valores positivos inteiros até
que um valor negativo seja informado. Ao final devem ser apresentados o
maior e menor valore informados pelo usuário.'''

maior = None
menor = None

while True:
    numeros = float(input("Digite um número: "))
    
    if numeros < 0:
        break

    if maior is None or numeros > maior:
        maior = numeros

    elif menor is None or numeros < menor:
        menor = numeros

if maior is not None and menor is not None:
    print("o maior: ", maior)
    print("o menor: ", menor)

else:
    print("nenhum valor positivo foi digitado!")