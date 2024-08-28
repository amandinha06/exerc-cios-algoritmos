'''Receber dois números e imprimi-los em ordem crescente. '''

menor = 0
maior = 0 

num1 = float(input("Digite o valor 1: "))
num2 = float(input("Digite o valor 2: "))

if num2 > num1:
    maior = num2
    menor = num1
else:
    maior = num1
    menor = num2

print("\n O maior número é: ", maior)
print("\n O menor número é: ", menor)

