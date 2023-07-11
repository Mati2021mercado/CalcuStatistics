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
    data_for_graphic = ([])
    titles = ['intervalo', 'punto_medio', 'frecuencia', 'frecuencia_acumulada']
    titles_graphic = ["intervalos","frecuencias"]
    for intervalo,pm,f,faa in zip(intervalos,PM_lista,F_lista,FAA_lista):
        pm = int(pm)
        
        datos = [intervalo, pm,f,faa]
        data_cuadro.append(datos)
        
        data_f_g = [intervalo,f]
        data_for_graphic.append(data_f_g)
        
    with open("calculos\\data.csv", 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows([titles])
        escritor_csv.writerows(data_cuadro)
        
    with open("calculos\\data_for_graphic.csv", 'w', newline='') as arch_csv:
        escritor_csv = csv.writer(arch_csv)
        escritor_csv.writerows([titles_graphic])
        escritor_csv.writerows(data_for_graphic)




# data = [
#     ["matias","mercado"]
# ]

# with open("calculos\\data.csv", 'w', newline='') as archivo_csv:
#     escritor_csv = csv.writer(archivo_csv)
#     escritor_csv.writerows(data)
