
# 1 - Escreva um programa para receber o nome de uma pessoa e imprimir uma saudação para ela na tela

msg="Olá! "
saudacao = input("Digite seu nome: ")
frase = msg + saudacao

print(frase)


# 2 - Escreva um programa para calcular o salário de uma trabalhadora baseado no número de horas que ela trabalhou e quanto ela ganha por hora.

print("Digite quanto você ganha por hora: ")
valor = input()
print("Digite quantas horas você trabalhou: ")
horas = input()

valor = float(valor)
horas = float(horas)

salario = valor * horas

print("Você receberá " + str(salario))

 
"""
3. Suponha que seja executado o seguinte código: (a) altura = 175 (b) peso = 12

Execute as seguintes operações e veja o resultado

1. width//2

2. width/2.0

3. height/3

4. 1 + 2 \* 5  """

width  = 175
height = 12


conta1 = width//2
print(conta1)

conta2 = width/2.0
print(conta2)

conta3 = height/3
print(conta3)

conta4 = 1 + 2 \
      *5
print(conta4)  


# 4. Escreva um programa para converter temperaturas de fahrenheit para celsius.


fahrenheit = input("Digite a temperatura em fahrenheit: ")
fahrenheit = float(fahrenheit)
celsius = (fahrenheit - 32)
print(celsius)
