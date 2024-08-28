'''Informe o tipo de carro (A, B e C). Informe o percurso rodado em km e
calcule o consumo estimado, conforme o tipo, sendo (A=8, B=9 e C=12)
km/litro'''

carro = str(input("Qual o tipo do seu carro(A, B OU C): "))
km = float(input("Quantos KM foram rodados?: "))

if carro == "A" or carro == "a":
    litros_por_km = 8 * km
    print(litros_por_km)
elif carro == "B" or carro == "b":
    litros_por_km = 9 * km
    print(litros_por_km)
elif carro == "C" or carro == "c":
    litros_por_km = 12 * km
    print(litros_por_km)