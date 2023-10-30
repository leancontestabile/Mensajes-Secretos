

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

    # recibe un mensaje , en caso de ser una letra o numero se "desplaza" una cantidad de veces a la derecha definido por el valor de clave,
    # en caso de ser un simbolo o espacio lo deja igual. para descifrar el mensaje se introduce una clave negativa

    """
    >>> cifrado_cesar("holaaBa##12",3)
    'kroddEd##45'

    >>> cifrado_cesar("kroddEd##45",-3)
    'holaaBa##12'

    >>> cifrado_cesar("algoritmos y programacion 1",4)
    'epksvmxqsw c tvskveqegmsr 5'

    >>> cifrado_cesar("epksvmxqsw c tvskveqegmsr 5",-4)
    'algoritmos y programacion 1'

    >>> cifrado_cesar("cifrado_cesar",17)
    'tzwiruf_tvjri'

    >>> cifrado_cesar("tzwiruf_tvjri",-17)
    'cifrado_cesar'

    >>> cifrado_cesar("mensajé_secreto N° 1222",18)
    'ewfksbw_kwujwlg F° 9000'

    >>> cifrado_cesar("ewfksbw_kwujwlg F° 9000",-18)
    'mensaje_secreto N° 1222'

    >>> cifrado_cesar("Hóla Este es mi menSaj3 secret0!",7)
    'Ovsh Lzal lz tp tluZhq0 zljyla7!'

    >>> cifrado_cesar("Ovsh Lzal lz tp tluZhq0 zljyla7!",-7)
    'Hola Este es mi menSaj3 secret0!'
    """

    LONGITUD_ALFABETO = 26
    LONGITUD_NUMEROS = 10

    mensaje_cifrado=""

    for caracter in mensaje:

        caracter_a_analizar = normalizar_caracter(caracter)

        if caracter_a_analizar.isalpha() and caracter_a_analizar != "ñ" and caracter_a_analizar != "Ñ":

            if caracter_a_analizar.islower():  
                nuevo_caracter = chr(ord("a") + ((ord(caracter_a_analizar)- ord("a")+clave) % LONGITUD_ALFABETO))  
            else:
                nuevo_caracter = chr(ord("A") + ((ord(caracter_a_analizar)- ord("A")+clave) % LONGITUD_ALFABETO))  

        elif caracter_a_analizar.isnumeric():
            nuevo_caracter = str((int(caracter_a_analizar)+clave)%LONGITUD_NUMEROS)
            
        else:
            nuevo_caracter = caracter_a_analizar

        mensaje_cifrado += nuevo_caracter


    return mensaje_cifrado


def main():
    import doctest
    cadena = "holaaBa##12"
    nueva_cadena = cifrado_cesar(cadena,3)
    print(nueva_cadena)
    print(cifrado_cesar(nueva_cadena,-3))
    print(doctest.testmod())
    

main()
