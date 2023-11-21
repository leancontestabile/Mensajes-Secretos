def cifrado_atbash(cadena):
    """
    Recibe una cadena por parametro y devuelve una cadena cifrada o descifrada con el metodo atbash
    
    El objetivo es cifrar o descifrar el mensaje que recibe la funcion, sustituyendo sus caracteres alfanumericos por su inverso
    
    Contestabile Leandro Ezequiel
    
    >>> cifrado_atbash("hola mundo")
    'SLOZ ÑFNWL'
    
    >>> cifrado_atbash("!hola#mundo$")
    '!SLOZ#ÑFNWL$'

    >>> cifrado_atbash("HOLA MUNDO")
    'sloz ñfnwl'
    
    >>> cifrado_atbash("0123 9876")
    '9876 0123'
    
    >>> cifrado_atbash("PEDROCARRASCO.ORG")
    'kvwilxziizhxl.lit'
    
    >>> cifrado_atbash("kvwilxziizhxl.lit")
    'PEDROCARRASCO.ORG'
    
    >>> cifrado_atbash("Somos el equipo Argentina")
    'hLÑLH VO VJFRKL zITVNGRNZ'
    
    >>> cifrado_atbash("Messi es el 10!")
    'ñVHHR VH VO 89!'
    
    >>> cifrado_atbash("hLÑLH XZÑKVLNVH WVO ÑFNWL")
    'Somos campeones del mundo'
    
    >>> cifrado_atbash("Pru3b4")
    'kIF6Y5'
    """
    
    lista_caracteres = []
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numeros_invertidos = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    letras_minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letras_invertidas_mayuscula = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    for letra in cadena:
        if letra.islower():
            lista_caracteres.append(letras_invertidas_mayuscula[letras_minuscula.index(letra)])
        elif letra.isupper():
            lista_caracteres.append(letras_minuscula[letras_invertidas_mayuscula.index(letra)])
        elif letra.isdigit():
            lista_caracteres.append(numeros[numeros_invertidos.index(letra)])
        else:
            lista_caracteres.append(letra)
    nueva_cadena = "".join(lista_caracteres)
    return nueva_cadena

def main():
    import doctest
    print(doctest.testmod())

main()
