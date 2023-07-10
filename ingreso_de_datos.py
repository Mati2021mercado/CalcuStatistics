#PARTO CON DATOS AGRUPADOS (VARIACION CONTINUA)

tamaño_de_la_muestra = int(input("sample size: "))

lista = ([])
intervalos = ([])
def Add_dict(cantidad):
    for i in range(cantidad):
        num1=int(input("num1: "))
        num2=int(input("num2: "))
        f=int(input("frecuencia: "))
        
        diccionario = {
            num1: num2,
            "frecuencia" : f
            }
        lista.append(diccionario)
        intervalo = f'{num1}-{num2}'
        intervalos.append(intervalo)

Add_dict(tamaño_de_la_muestra)
