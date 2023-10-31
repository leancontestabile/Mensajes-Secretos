

def normalizar_mensaje(mensaje):
    #recibe un mensaje y convierte las vocales tildadas en vocales sin tildar y las "ñ" en "ni", el resto de caracteres los deja igual
    
    vocales_tildadas = ['á', 'é', 'í', 'ó', 'ú','Á','É','Í','Ó','Ú']
    vocales_sin_tildar = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    
    mensaje_a_analizar=""
    
    for caracter in mensaje:
        if caracter == "ñ":
            nuevo_caracter = "ni"
        elif caracter == "Ñ":
            nuevo_caracter = "NI"
        elif caracter in vocales_tildadas:
                indice = vocales_tildadas.index(caracter)
                nuevo_caracter = vocales_sin_tildar[indice]
        else:
            nuevo_caracter = caracter
        mensaje_a_analizar += nuevo_caracter
        
    return mensaje_a_analizar




def cifrado_cesar(mensaje, clave):

    # recibe un mensaje , en caso de ser una letra o numero se "desplaza" una cantidad de veces a la derecha definido por el valor de clave,
    # en caso de ser un simbolo o espacio lo deja igual. para descifrar el mensaje se introduce una clave negativa
    
    #funcion hecha por Conde Brian Agustin

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
    
    mensaje_a_analizar = normalizar_mensaje(mensaje)
    for caracter in mensaje_a_analizar:
        
        if caracter.isalpha():

            if caracter.islower():  
                nuevo_caracter = chr(ord("a") + ((ord(caracter)- ord("a")+clave) % LONGITUD_ALFABETO))  
            else:
                nuevo_caracter = chr(ord("A") + ((ord(caracter)- ord("A")+clave) % LONGITUD_ALFABETO))  

        elif caracter.isnumeric():
            nuevo_caracter = str((int(caracter)+clave)%LONGITUD_NUMEROS)
            
        else:
            nuevo_caracter = caracter

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
