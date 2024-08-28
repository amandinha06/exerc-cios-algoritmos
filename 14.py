salario = float(input("Digite qual seu salário: "))
prestacao = float(input("Digite qual o valor que deseja para o emprestimo: "))

porcentagem = (salario / 100) * 20 

if prestacao > porcentagem:
    print("Esse emprestimo não pode ser concedido.")
    
else: 
    print("Esse emprestimo pode ser concedido. ")