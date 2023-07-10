import sys
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')

from media import media
from population_standard_deviation import desvio

cv = desvio / media
cv = round(cv, 3)
    




