from calculos.input import lista

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
        if key == "frecuency":
            f = value
            F_lista.append(f)
        else:
            a = float(key)
            b = float(value)

            #SACO PUNTO MEDIO (PM)
            pm = (a + b) / 2
            # print(float(pm))
            PM_lista.append(pm)
            
            # print(f'X: {a} - {b} PM: {int(pm)} ')