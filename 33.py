'''Escrever um programa que leia, valores inteiros, até ser lido o valor 99.
Quando isso acontecer o programa deverá escrever a soma e a média dos
valores lidos.'''

soma = 0 
contador = 0 

while True:
    valor = float(input("Entre com um valor positivio para iniciar o loop: "))
    
    if valor == 99:
        print("O valor digitado foi 99.")
        break

    soma = soma + valor
    contador = contador + 1
    media = soma / contador

    print("A soma é: ", soma)
    print("A média é: ", media)