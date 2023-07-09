from data_and_frequency import PM_lista, F_lista


    ###########################################################
    ######### CALCULO la suma de todas las f * pm #############
    ###########################################################
    

#RECORRO F_LISTA Y PM_LISTA A LA VEZ Y EN UNA NUEVA LISTA VOY GUARDANDO LOS REUSLTADOS DE LA MULTIPLICACION DE LOS ITEMS: F * PM

pm_por_f = ([])
for pm,f in zip(PM_lista,F_lista):
    calculo = pm * f
    pm_por_f.append(calculo)

la_suma_pm_por_f = sum(pm_por_f) 