from calculos.data_and_frequency import PM_lista, F_lista
from calculos.mean import media


    ###############################################################################################
    ######### CALCULO pm_menos_la_media_todo_elevado_al_cuadrado_menos_la_frecuencia ##############
    ###############################################################################################
    



pm_media_f = ([])
for pm,f in zip(PM_lista,F_lista):
    calculo = ((pm - media)**2) * f
    pm_media_f.append(calculo)

la_suma_pm_media_f = sum(pm_media_f)


