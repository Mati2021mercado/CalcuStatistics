question = input("Is the data set population? (yes or not): ")
question = question.lower()


if question == "yes":
    import calculos.cv_poblacion as cv_poblacion
    # from visualitation import visualitation_data
    from calculos.visualitation import visualitation_data
    from calculos.ingreso_de_datos import tamaño_de_la_muestra
    from calculos.data_visualitation import cuadro
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
    import calculos.cv_muestra as cv_muestra
    from calculos.visualitation import visualitation_data
    from calculos.ingreso_de_datos import tamaño_de_la_muestra
    from calculos.data_visualitation import cuadro
    # from grafico import Graphic
    
    visualitation_data(
        cv = cv_muestra.cv,
        desvio = cv_muestra.desvio,
        media = cv_muestra.media,
        tamaño = tamaño_de_la_muestra
        )
    cuadro()
    # Graphic()
    
else:
    print("you entered the data wrong")
