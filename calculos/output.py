from calculos.data_and_frequency import F_lista, PM_lista
from calculos.frequency_accumulated import FAA_lista
from calculos.input import limite_inferior, limite_superior
from calculos.check_without_decimals import tiene_un_solo_cero_decimal
# import pandas as pd

import csv

    ##############################################
    ######### VIZAULIZACION DE LA DATA ###########
    ##############################################

# RECORRER LAS 3 LISTAS A LA VEZ PARA MOSTRAR EL CUADRO
def cuadro():
    data_cuadro = ([])
    data_for_graphic = ([])
    
    titles = ['limite_inferior', 'limite_superior', 'punto_medio', 'frecuencia', 'frecuencia_acumulada']
    
    titles_graphic = ["intervalos","frecuencias"]
    
    for LI,LS,pm,f,faa in zip(limite_inferior, limite_superior,PM_lista,F_lista,FAA_lista):
        #PREPARO LOS DATOS PARA data.csv
        datos = [LI,LS, pm,f,faa]
        data_cuadro.append(datos)
        
        #PREPARO LOS DATOS PARA data_for_graphic.csv
        intervalos = f'{tiene_un_solo_cero_decimal(LI)}-{tiene_un_solo_cero_decimal(LS)}'
        data_f_g = [intervalos,f]
        data_for_graphic.append(data_f_g)
        
    with open("archivos\\data.csv", 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows([titles])
        escritor_csv.writerows(data_cuadro)
        
        
    with open("archivos\\data_for_graphic.csv", 'w', newline='') as arch_csv:
        escritor_csv = csv.writer(arch_csv)
        escritor_csv.writerows([titles_graphic])
        escritor_csv.writerows(data_for_graphic)




# data = [
#     ["matias","mercado"]
# ]

# with open("calculos\\data.csv", 'w', newline='') as archivo_csv:
#     escritor_csv = csv.writer(archivo_csv)
#     escritor_csv.writerows(data)
