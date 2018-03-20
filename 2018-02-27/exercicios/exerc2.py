"""
2. Reescreva o programa acima com try-except. Assim se o usuário 
não digitar um valor o programa termina com uma mensagem de erro.
"""
try:
    horas = input("Digite a quantidade de horas trabalhadas: ")
    valor = input("Digite o valor da hora trabalha: ")
    salario = 0
    horas = int(horas)
    valor = float(valor)

    if (horas>40):
        extra=(valor*1.5)*(horas-40)
        salario=(valor*40)
        salario=(salario+extra)         
    else:
        salario = (horas * valor)
    print("O valor do salário a ser recebido é: " + str(salario))
        
except:
    print("ERRO! Digitou errado e/ou não digitou! ")