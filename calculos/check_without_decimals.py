def tiene_un_solo_cero_decimal(numero):
    # Convertir el número a cadena
    numero_str = str(numero)
    
    # Encontrar la posición del punto decimal
    punto_pos = numero_str.find('.')
    
    # Verificar si hay un punto decimal y al menos un dígito después de él
    if punto_pos != -1 and punto_pos < len(numero_str) - 1:
        # Verificar si hay exactamente un cero después del punto decimal
        if numero_str[punto_pos+1] == '0' and numero_str[punto_pos+2:] == '':
            return int(numero)
    
    return numero

# Ejemplos de uso
# numero1 = 5.0
# numero2 = 5.01

# print(tiene_un_solo_cero_decimal(numero1))  # Salida: True
# print(tiene_un_solo_cero_decimal(numero2))  # Salida: False
