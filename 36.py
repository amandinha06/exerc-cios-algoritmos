'''Escrever um programa que receba vários números inteiros no teclado e no
final imprimir a média dos números múltiplos de 3. Para sair digitar 0
(zero). '''

soma = 0 
contador = 0 

while True:
    valor = float(input("Entre com um valor positivio para iniciar o loop(Digite 0 para sair): "))

    if valor == 0:
        break

    soma = soma + valor
    contador = contador + 1
    media = soma / contador

    if valor % 3 == 0:
        print("A soma é: ", soma)
        print("A média é: ", media)
    
    else:
        print("Valor não é multiplo por 3!")