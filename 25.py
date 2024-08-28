'''Um comerciante comprou um produto e quer vendê-lo com lucro de 5% se
o valor da compra for menor que 20,00; caso contrário, o lucro será de
30%. Entrar com o valor do produto e imprimir o valor da venda.
'''

valor = float(input("Qual o valor do produto? "))

cinco = (valor / 100) * 5
trinta = (valor / 100) * 30 

if valor < 20:
    valor += cinco
    print("O valor será de: ", valor)

else:
    valor += trinta
    print("O valor será de: ", valor)