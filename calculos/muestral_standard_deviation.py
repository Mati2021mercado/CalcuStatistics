import sys
# import math
from math import sqrt
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')

from calcula_la_suma_de_todos_los_pm_menos_la_media_todo_elevado_al_cuadrado_por_la_frecuencia import la_suma_pm_media_f
from n import n

# print(la_suma_pm_media_f)
# print(n)

desvio_muestral_al_cuadrado = la_suma_pm_media_f / n - 1 

desvio_muestral = sqrt(desvio_muestral_al_cuadrado)

print(f'el desvio estandar es de: {desvio_muestral}')