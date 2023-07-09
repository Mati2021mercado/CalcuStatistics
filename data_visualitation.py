from data_and_frequency import F_lista, PM_lista
from frequency_accumulated import FAA_lista


    ##############################################
    ######### VIZAULIZACION DE LA DATA ###########
    ##############################################

# RECORRER LAS 3 LISTAS A LA VEZ PARA MOSTRAR EL CUADRO
for pm,f,faa in zip(PM_lista,F_lista,FAA_lista):
    print(f'PM: {pm}, F: {f}, FAA: {faa}')