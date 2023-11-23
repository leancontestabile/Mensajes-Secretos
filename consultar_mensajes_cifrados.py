def consultar_mensajes(id_usuario):

    """

    Recibe una cadena por parametro, devuelve una lista y un entero

    El objetivo es abrir el archivo, verificar en el mismo los mensajes que son para el y guardarlos

    Contestabile Leandro Ezequiel

    """

    mensajes_generales = []
    mensajes_personales = []
    total_mensajes = 0

    with open("prueba_mensajes.csv", "r") as ar_mensajes:
        for linea in ar_mensajes:
            emisor, receptor, cifrado, mensaje_cifrado = linea.rstrip("\n").split(",")
            if (receptor == id_usuario):
                if (cifrado == "A"):
                    mensaje_descifrado = cifrado_atbash(mensaje_cifrado)
                    aux_mensaje = emisor +": " + mensaje_descifrado
                    mensajes_personales.append(aux_mensaje)
                else:
                    mensaje_descifrado = cifrado_cesar(mensaje_cifrado, -int(cifrado[1]))
                    aux_mensaje = emisor +": " + mensaje_descifrado
                    mensajes_personales.append(aux_mensaje)
                total_mensajes += 1
            elif (receptor == "*") and (emisor != id_usuario):
                if (cifrado == "A"):
                    mensaje_descifrado = cifrado_atbash(mensaje_cifrado)
                    aux_mensaje = "#" + emisor +": " + mensaje_descifrado
                    mensajes_generales.append(aux_mensaje)
                else:
                    mensaje_descifrado = cifrado_cesar(mensaje_cifrado, -int(cifrado[1]))
                    aux_mensaje = "#" + emisor +": " + mensaje_descifrado
                    mensajes_generales.append(aux_mensaje)
                total_mensajes += 1

    mensajes_usuario = mensajes_generales + mensajes_personales

    return mensajes_usuario, total_mensajes
