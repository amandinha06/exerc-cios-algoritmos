'''Solicitar um número entre 1 e 4. Se a pessoas digitar um número
diferente, mostrar a mensagem "entrada inválida" e solicitar o número
novamente. Se digitar correto mostrar o número digitado. '''

while True:
    num = float(input("Digite um número entre 1 e 4: "))
    
    if 1 <= num <= 4 : 
        print("Entrada válida!")
        break
    else: 
        print("Entrada inválida!")