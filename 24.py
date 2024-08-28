'''Receber um número do teclado e informar se ele é divisível por 10, por 5,
por 2 ou se não é divisível por nenhum destes.'''

num = float(input("Digite um  número: "))

if num % 10 == 0:
    print("Divisível por 10")

elif num % 5 == 0:
    print("Divisível por 5")

elif num % 2 == 0:
    print("Divisível por 2")

else:
    print("Divisível por outro numero")