import sys
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')

import csv

def visualitation_data(cv,desvio,media,tamaño):
    data = f'''
      Size          : {tamaño}
      Deviation     : {desvio}
      CV            : {cv}
      Mean/average  : {media}
      '''
    with open("calculos\\data.txt",'w',encoding="UTF-8",) as archivo:
        archivo.write(f"{data}")
    
    
    # with open("aprendiendo1\\archivos\\data.txt",'w',encoding="UTF-8") as archivo:


