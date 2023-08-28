from calculos.data_and_frequency import F_lista

#Hago la lista de Frecuencias Acumuladas(FAA)

#LISTA FAA = QUE VAYA SUMANDO LAS Frecuencias (F) de la lista F_LISTA y vaya mostrando el resultado de cada suma

FAA_lista = ([])

FAA = 0
for num in F_lista:
    
    FAA += num
    FAA_lista.append(FAA)