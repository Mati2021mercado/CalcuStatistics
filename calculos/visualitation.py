import sys
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')



def visualitation_data(cv,desvio,media,tamaño):
    data = f'''
      Size              :{tamaño}
      Min               :{1}
      Max               :{1}
      Deviation         :{desvio}
      CV                :{cv}
      Mean/average      :{media}
      Median            :{1}
      Mode              :{1}
      '''
    print(data)
