question = input("Is the data set population? (yes or not): ")
question = question.lower()


if question == "yes":
    import calculos.cv_population as cv_population
    from calculos.visualitation_for_txt import visualitation_data
    from calculos.input import tamaño_de_la_muestra
    from calculos.output import cuadro
    from App_graphic import Graphic
    
    visualitation_data(
        cv = cv_population.cv,
        desvio = cv_population.desvio,
        media = cv_population.media,
        tamaño = tamaño_de_la_muestra
        )
    cuadro()
    
elif question == "not":
    import calculos.cv_sample as cv_sample
    from calculos.visualitation_for_txt import visualitation_data
    from calculos.input import tamaño_de_la_muestra
    from calculos.output import cuadro
    from App_graphic import Graphic
    
    visualitation_data(
        cv = cv_sample.cv,
        desvio = cv_sample.desvio,
        media = cv_sample.media,
        tamaño = tamaño_de_la_muestra
        )
    cuadro()
    
else:
    print("you entered the data wrong")
