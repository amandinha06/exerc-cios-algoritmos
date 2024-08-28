'''Entrar com um número e imprimir a raiz quadrada do número. Caso ele
seja positivo. E o quadrado dele caso seja negativo.'''

num = float(input("Digite um numero: "))

if num > 0:
    raiz = num * 0.5
    print(raiz)
else: 
    dobro = num * num 
    print(dobro)