import sys
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')

from media import media
from muestral_standard_deviation import desvio

cv = desvio / media
cv = cv.round(cv, 3)