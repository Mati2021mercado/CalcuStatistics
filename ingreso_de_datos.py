#PARTO CON DATOS AGRUPADOS (VARIACION CONTINUA)

tamaño_de_la_muestra = int(input("number of intervals: "))

lista = ([])
limite_inferior = ([])
limite_superior = ([])

def Add_dict(cantidad):
    for i in range(cantidad):
        LI=float(input("lower limit: "))
        LS=float(input("upper limit: "))
        f=int(input("frecuency: "))
        
        diccionario = {
            LI: LS,
            "frecuency" : f
            }
        lista.append(diccionario)
        # intervalo = f'{LI}-{LS}'
        # intervalos.append(intervalo)
        limite_inferior.append(LI)
        limite_superior.append(LS)

Add_dict(tamaño_de_la_muestra)
