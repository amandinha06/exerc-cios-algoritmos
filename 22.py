soma = 0 
contador = 0 

while True:
    numeros = float(input("Digite um número: "))
    
    if numeros < 0:
        break
    
    soma = soma + numeros
    contador = contador + 1
    media = soma / contador
    
   

print("A soma é: ", soma)
print("A média é: ", media)
print("O total de valores lidos é: ", contador)

