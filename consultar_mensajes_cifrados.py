def consultar_mensajes(id_usuario):
#     implementacion funciones y agregar docstring
    mensajes_generales = []
    mensajes_personales = []
    total_mensajes = 0
    print("Lista de mensajes:")
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
    for i in mensajes_generales:
        print(i)
    for i in mensajes_personales:
        print(i)
    print("Total de mensajes:", total_mensajes)
