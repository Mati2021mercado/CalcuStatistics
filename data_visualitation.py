from data_and_frequency import F_lista, PM_lista
from frequency_accumulated import FAA_lista
from ingreso_de_datos import intervalos
# import pandas as pd
import csv

    ##############################################
    ######### VIZAULIZACION DE LA DATA ###########
    ##############################################

# RECORRER LAS 3 LISTAS A LA VEZ PARA MOSTRAR EL CUADRO
def cuadro():
    data_cuadro = ([])
    titles = ['intervalo', 'punto medio', 'frecuencia', 'frecuencia acumulada']
    for intervalo,pm,f,faa in zip(intervalos,PM_lista,F_lista,FAA_lista):
        pm = int(pm)
        
        datos = [intervalo, pm,f,faa]
        data_cuadro.append(datos)
        
    with open("calculos\\data.csv", 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
            # escritor_csv.write
        escritor_csv.writerows([titles])
        escritor_csv.writerows(data_cuadro)




# data = [
#     ["matias","mercado"]
# ]

# with open("calculos\\data.csv", 'w', newline='') as archivo_csv:
#     escritor_csv = csv.writer(archivo_csv)
#     escritor_csv.writerows(data)
