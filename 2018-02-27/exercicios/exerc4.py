"""
4. Escreva um programa para ordenar 3 números em ordem crescente. 
   Os números devem ser digitados pelo usuário. Não utilize condicionais compostas.
"""
numero = [1,2,3]

for i in range(0,3):
    numero[i] = int(input("Digite um numero: "))
    
numero = sorted(numero)

print("números ordenados: " + str(numero))

