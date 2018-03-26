import csv

with open('remuneracoes.csv', 'r') as f: # Somente r para leitura do arquivo
      list1 = [tuple(line.values()) for line in csv.DictReader(f)]

      for linha in list1:
      	print(linha)