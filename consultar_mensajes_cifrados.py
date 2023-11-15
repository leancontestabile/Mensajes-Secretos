def consultar_mensajes(id_usuario):
    total_mensajes = 0
    print("Lista de mensajes:")
    with open("prueba_mensajes.csv", "r") as ar_mensajes:
        for linea in ar_mensajes:
            emisor, receptor, cifrado, mensaje_cifrado = linea.rstrip("\n").split(",")
            if (receptor == id_usuario):
                if (cifrado == "A"):
                    mensaje_descifrado = cifrado_atbash(mensaje_cifrado)
                    print(emisor,":", mensaje_descifrado)
                else:
                    mensaje_descifrado = cifrado_cesar(mensaje_cifrado, -int(cifrado[1]))
                    print(emisor,":", mensaje_descifrado)
                total_mensajes += 1
            elif (receptor == "*") and (emisor != id_usuario):
                if (cifrado == "A"):
                    mensaje_descifrado = cifrado_atbash(mensaje_cifrado)
                    print("#",emisor,":", mensaje_descifrado)
                else:
                    mensaje_descifrado = cifrado_cesar(mensaje_cifrado, -int(cifrado[1]))
                    print("#",emisor,":", mensaje_descifrado)
                total_mensajes += 1
    print("Total de mensajes:", total_mensajes)
