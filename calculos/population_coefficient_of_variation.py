import sys
# import math
from math import sqrt
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')

from media import media
from desvio import desvio


cv = desvio / media

print(f'el coeficiente de variacion es de: {cv}')