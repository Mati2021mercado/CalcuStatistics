import csv

def Result(k):
    datos = []
    #################
    #################   RECORRO EL ARCHIVO CSV CON LOS DATOS AGRUPADOS
    #################
        
    # Abre el archivo CSV en modo de lectura
    with open('archivos/data.csv', 'r') as archivo_csv:
        # Crea un objeto de lectura CSV
        lector_csv = csv.reader(archivo_csv)
        
        # Ignora la primera fila
        next(lector_csv)
        # Inicializa una lista para almacenar los datos
        
        # Itera a través de las filas restantes en el archivo CSV
        for fila in lector_csv:
            # Convierte los valores de cadena a tipos adecuados si es necesario
            limite_inferior = float(fila[0])
            limite_superior = float(fila[1])
            punto_medio = float(fila[2])
            frecuencia = int(fila[3])
            frecuencia_acumulada = int(fila[4])
            
            # Agrega los datos a la lista
            datos.append([limite_inferior, limite_superior, punto_medio, frecuencia, frecuencia_acumulada])



    #################
    #################   LE AGREGO UN INDICE A LA LISTA DE DATOS
    #################

    for indice, sublist in enumerate(datos):
        sublist.insert(0, indice)


    #################
    #################   AGREGO EL LOCALIZADOR CON K (PERCENTIL) QUE ME VA A POSICIONAR EN LA "TABLA"
    #################


    ultimo_conjunto = datos[-1]  # Accede al último conjunto en la lista
    ultimo_valor = ultimo_conjunto[-1]

    n = ultimo_valor
    localizador = (k * n)/100



    #################
    #################   UNA VEZ POSICIONADO EN LA "TABLA" EXTRAIGO LOS DATOS QUE NECESITO Y APLICO LA FORMULA ESTADISTICA
    #################



    for i in datos:
        if i[-1] > localizador:
            print(f'FAA: {i[-1]} {i} index: {i[0]}')
            index = i[0]
            frecuencia = i[4]
            LI = i[1]
            LS = i[2]
            intervalo = LS - LI
            
            #PARA OBTENER LA FAA ANTERIOR (DE LA FILA QUE ESTA ARRIBA) LE RESTO 1 AL INDICE ACTUAL Y VUELVO A RECORRERLO HASTA QUE DE CON EL QUE SEA IGUAL QUE LA RESTA (VUELVO 1 HACIA ATRAS)
            for el in datos:
                if el[0] == (index - 1):
                    faa_ant = el[-1]
                    
            calculo = LI + (((localizador - faa_ant)/frecuencia) * intervalo)
            
            print(f'''
                Frecuencia: {frecuencia}
                Limite Inferior: {LI}
                Limite Superior: {LS}
                Intervalo: {intervalo}
                FAA Ant: {faa_ant}
                
                Resultado: {calculo}
                
                Formula: LI + ( ( (localizador - faa_ant) / frecuencia) * intervalo)
                        {LI} + ( ( (    {localizador}  -  {faa_ant} )    /    {frecuencia}      ) * {intervalo}      )
                ''')
            
            
            break