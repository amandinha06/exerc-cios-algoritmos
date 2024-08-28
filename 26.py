'''Receber do teclado, vários números e verificar se eles são ou não
quadrados perfeitos. O programa termina quando o usuário digitar um
número menor ou igual a zero.
'''

valor = float(input("Entre com um valor positivio para iniciar o loop: "))
raiz = int(valor ** 0.5)
if raiz * raiz == valor:
    print("\n Esse número é um quadrado perfeito")

while valor > 0:
    valor = float(input("Entre com um valor positivio para iniciar o loop ou negativo para interromper: "))

    raiz = int(valor ** 0.5)
    if raiz * raiz == valor:
        print("\n Esse número é um quadrado perfeito")

    if raiz * raiz != valor:
        print("\n Esse número não é um quadrado perfeito")

    if valor <= 0:
        break