#PARTO CON DATOS AGRUPADOS (VARIACION CONTINUA)

lista = ([])

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
Add_dict(5)