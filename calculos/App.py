import sys
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')


question = input("Is the data set population? (yes or not): ")
question = question.lower()


if question == "yes":
    import cv_poblacion
    from visualitation import visualitation_data
    from ingreso_de_datos import tamaño_de_la_muestra
    from data_visualitation import cuadro
    # from grafico import Graphic
    
    visualitation_data(
        cv = cv_poblacion.cv,
        desvio = cv_poblacion.desvio,
        media = cv_poblacion.media,
        tamaño = tamaño_de_la_muestra
        )
    cuadro()
    # Graphic()
    
    
elif question == "not":
    import cv_muestra
    from visualitation import visualitation_data
    from ingreso_de_datos import tamaño_de_la_muestra
    from data_visualitation import cuadro
    from grafico import Graphic
    
    visualitation_data(
        cv = cv_muestra.cv,
        desvio = cv_muestra.desvio,
        media = cv_muestra.media,
        tamaño = tamaño_de_la_muestra
        )
    cuadro()
    Graphic()
    
else:
    print("you entered the data wrong")
