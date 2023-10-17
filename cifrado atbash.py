def cifrado_atbash(cadena):
    lista_caracteres = []
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numeros_invertidos = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    letras_minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letras_invertidas_mayuscula = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "Ñ", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    for letra in cadena:
        if letra.islower():
            lista_caracteres.append(letras_invertidas_mayuscula[letras_minuscula.index(letra)])
        elif letra.isupper():
            lista_caracteres.append(letras_minuscula[letras_invertidas_mayuscula.index(letra)])
        elif letra.isdigit():
            lista_caracteres.append(numeros[numeros_invertidos.index(letra)])
        elif letra not in letras_minuscula:
            lista_caracteres.append(letra)
            
    nueva_cadena = "".join(lista_caracteres)
    print(nueva_cadena)

def main():
    cifrado_atbash("hola mundo")
    cifrado_atbash("!hola#mundo$")
    cifrado_atbash("HOLA MUNDO")
    cifrado_atbash("0123 9876")
    cifrado_atbash("PEDROCARRASCO.ORG")
    cifrado_atbash("kvwilxziizhxl.lit")

main()