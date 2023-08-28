
from math import sqrt


from calculos.calcula_la_suma_de_todos_los_pm_menos_la_media_todo_elevado_al_cuadrado_por_la_frecuencia import la_suma_pm_media_f
from calculos.n import n

desvio_al_cuadrado = la_suma_pm_media_f / n - 1 

desvio = sqrt(desvio_al_cuadrado)
desvio = round(desvio, 3)