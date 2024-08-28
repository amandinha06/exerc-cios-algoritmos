''' Ler um número inteiro e verificar se está compreendido entre 20 e 80. Se
tiver, imprimir “parabéns”, senão imprimir “chimpanzé”'''

num = int(input("Digite um número inteiro entre 20 e 80: "))

if 20 <= num <= 80:
    print("parabéns")
else:
    print("chimpanzé")