import sys
# print(sys.path)
sys.path.append('C:\\Users\\Matias\\Desktop\\Lenguajes\\Python\\CalcuStatistics')


respuesta = input('los datos agrupados ¿son poblacionales? ')

respuesta = respuesta.lower()


if respuesta == "yes" or "si":
    from media import media
    from population_standard_deviation import desvio_poblacional
    cv = desvio_poblacional / media
    print(f'el coeficiente de variacion (poblacional) es: {cv}')
    print(f'la media es: {media}')
elif respuesta == "no" or "not":
    from media import media
    from muestral_standard_deviation import desvio_muestral
    cv = desvio_muestral / media
    print(f'el coeficiente de variacion (muestral) es: {cv}')
    print(f'la media es: {media}')
else :
    print("ininteligible")

# 


