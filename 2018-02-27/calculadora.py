# encoding: utf-8
# Programa de uma calculadora de operações básicas
# Paulo Sérgio do Nascimento 160013-3   27/02/2018

num1 = input ("Digite o primeiro número: ")
num2 = input ("Digite o segundo número: ")
res = ""
oper = input ("Digite a operação (+, -, *, /): ")

if oper == '+' :
   res = float(num1) + float(num2)

elif oper == '-':
     res = float(num1) - float(num2)

elif oper == '*':
     res = float(num1) * float(num2)	 

elif oper == '/':
	 res = float(num1) / float(num2)


print(res)