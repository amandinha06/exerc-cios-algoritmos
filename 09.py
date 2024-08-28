hora_aula = float(input('Qual o valor da hora aula? '))
qnt_aulas = int(input('Qual o número total de aulas dadas? '))
valor_inss = float(input('Digite a porcentagem do INSS: '))

valores = hora_aula * qnt_aulas
calculo = (valores / 100) * valor_inss
total = valores - calculo 

print("Seu salário será no valor de: ", total)