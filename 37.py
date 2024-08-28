'''Ler um número do teclado e imprimir todos os números de 1 até o número
lido. Imprimir o produto dos números.'''

num = int(input("Digite o número final: "))

for i in range(1, num):
    produto = 1 * num
    print(i)
print("o produto é: ", produto)