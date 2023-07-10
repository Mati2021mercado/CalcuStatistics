import sys
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')


question = input("Is the data set population? (yes or not): ")
question = question.lower()


if question == "yes":
    import cv_poblacion
    from visualitation import visualitation_data
    from ingreso_de_datos import tamaño_de_la_muestra
    
    visualitation_data(
        cv = cv_poblacion.cv,
        desvio = cv_poblacion.desvio,
        media = cv_poblacion.media,
        tamaño = tamaño_de_la_muestra
        )
    
elif question == "not":
    import cv_muestra
    from visualitation import visualitation_data
    from ingreso_de_datos import tamaño_de_la_muestra
    
    visualitation_data(
        cv = cv_muestra.cv,
        desvio = cv_muestra.desvio,
        media = cv_muestra.media,
        tamaño = tamaño_de_la_muestra
        )
    
else:
    print("you entered the data wrong")

# cv = 0

# if question == "si":
    
#     cv = 1
    
# elif question == "no":
#     cv = 2
    
# print(cv)