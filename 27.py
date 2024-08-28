''' Ler 2 valores e somar os dois. Caso a soma seja maior que 10, mostrar a
soma.'''

num1 = float(input('Digite o numero 1: '))
num2 = float(input('Digite o numero 2: '))

soma = num1 + num2

if soma > 10:
    print(soma)
else:
    print("não foi possível fazer a soma.")