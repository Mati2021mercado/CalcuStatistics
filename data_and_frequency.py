from ingreso_de_datos import lista

    ###########################
    ######### PARTE 2 #########
    ###########################
    #hago la lista de Frecuencias y la lista de PM

#lISTA VACIA DE FAA
#FAA = LA SUMA DE LAS FRECUENCIAS
F_lista = ([]) 
#LISTA VACIA DE PM
PM_lista = ([])

#ACCEDO A CADA DICCIONARIO Y GUARDO LOS DATOS EN LAS LISTAS VACIAS PM_LISTA Y F_LISTA
for datos_agrupados in lista :
    for datos in datos_agrupados.items():
        key = datos[0]
        value = datos[1]
        if key == "frecuencia":
            f = value
            F_lista.append(f)
        else:
            a = key
            b = value

            #SACO PUNTO MEDIO (PM)
            pm = (a + b) / 2
            PM_lista.append(pm)
            # print(f'X: {a} - {b} PM: {int(pm)} ')