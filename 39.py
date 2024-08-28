'''Solicitar a idade de várias pessoas e imprimir: Total de pessoas com menos
de 21 anos. Total de pessoas com mais de 50 anos. O programa termina
quando idade for = 99.'''

soma = 0
contador_1 = 0
contador_2 = 0 

while True:
    idade = float(input("Digite sua idade: "))

    if idade == 99:
        print("Idade inválida.")
        break

    if idade <= 21:
        contador_1 += 1
    
    elif idade >= 50:
        contador_2 += 1
    
    print("Pessoas com menos de 21 anos: ", contador_1)
    print("Pessoas com mais de 50 anos: ", contador_2)

