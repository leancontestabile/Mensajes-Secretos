
import doctest



def normalizar_caracter(caracter):

    
    vocales_tildadas = ['á', 'é', 'í', 'ó', 'ú','Á','É','Í','Ó','Ú']
    vocales_sin_tildar = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

    if caracter in vocales_tildadas:
            indice = vocales_tildadas.index(caracter)
            nueva_letra = vocales_sin_tildar[indice]
            caracter_a_analizar = nueva_letra
    else:
        caracter_a_analizar = caracter
    
    return caracter_a_analizar




def cifrado_cesar(mensaje, clave):

    """
    >>> cifrado_cesar("holaaBa##12",3)
    'krñddEd##45'

    >>> cifrado_cesar("krñddEd##45",-3)
    'holaaBa##12'

    >>> cifrado_cesar("algoritmos y programacion 1",4)
    'eoksvmxpsw c tvskvepegmsq 5'

    >>> cifrado_cesar("eoksvmxpsw c tvskvepegmsq 5",-4)
    'algoritmos y programacion 1'

    >>> cifrado_cesar("cifrado_cesar",17)
    'syviqtf_sujqi'

    >>> cifrado_cesar("syviqtf_sujqi",-17)
    'cifrado_cesar'

    >>> cifrado_cesar("mensaje_secreto N° 1222",18)
    'dvekrav_kvtjvlg E° 9000'

    >>> cifrado_cesar("dvekrav_kvtjvlg E° 9000",-18)
    'mensaje_secreto N° 1222'

    >>> cifrado_cesar("Hola Este es mi menSaj3 secret0!",7)
    'Ñvrh Lzal lz so sltZhp0 zljyla7!'

    >>> cifrado_cesar("Ñvrh Lzal lz so sltZhp0 zljyla7!",-7)
    'Hola Este es mi menSaj3 secret0!'
    """

  
    lista_abecedario_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_abecedario_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    vocales_tildadas = ['á', 'é', 'í', 'ó', 'ú','Á','É','Í','Ó','Ú']
    vocales_sin_tildar = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

    mensaje_cifrado = ''
    longitud_alfabeto = len(lista_abecedario_minusculas)
    LONGITUD_NUMEROS = 10

    for caracter in mensaje:

        caracter_a_analizar = normalizar_caracter(caracter)
        
        if caracter_a_analizar.isalpha():
            if caracter_a_analizar.islower():

                indice_caracter = lista_abecedario_minusculas.index(caracter_a_analizar)
                nuevo_indice = (indice_caracter + clave)%longitud_alfabeto
                nuevo_caracter = lista_abecedario_minusculas[nuevo_indice]
            else:
                indice_caracter = lista_abecedario_mayusculas.index(caracter_a_analizar)
                nuevo_indice = (indice_caracter + clave)%longitud_alfabeto
                nuevo_caracter = lista_abecedario_mayusculas[nuevo_indice]

        elif caracter_a_analizar.isnumeric():
            nuevo_caracter = str((int(caracter_a_analizar)+clave)%LONGITUD_NUMEROS)

        else:
            nuevo_caracter = caracter_a_analizar

        mensaje_cifrado += nuevo_caracter

    return mensaje_cifrado


def main():
    cadena = "holaaBa##12ñ"
    nueva_cadena = cifrado_cesar(cadena,3)
    print(nueva_cadena)
    print(cifrado_cesar(nueva_cadena,-3))
    

main()
doctest.testmod()