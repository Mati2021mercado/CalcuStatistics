
from math import sqrt

from calculos.calculation__Σ_PM_menos_la_MEAN_todo_elevado_al_cuadrado_por_la_F__ import la_suma_pm_media_f
from calculos.n import n

desvio_al_cuadrado = la_suma_pm_media_f / n

desvio = sqrt(desvio_al_cuadrado)
desvio = round(desvio, 3)
