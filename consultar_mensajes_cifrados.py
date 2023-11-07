def consultar_mensajes(id_usuario):
    total_mensajes = 0
    print("Lista de mensajes:")
    
    #leer linea del archivo
    with open("prueba_mensajes.csv", "r") as ar_mensajes:
        for linea in ar_mensajes:
            emisor, receptor, cifrado, mensaje_cifrado = linea.rstrip("\n").split(",")
            print(emisor, receptor, cifrado, mensaje_cifrado)
    
    #verificar que el mensaje sea para el (si el mensaje es un all anteponer un # al id del remitente)
    #mostrarlo descifrado
    print("Total de mensajes:", total_mensajes)
    
consultar_mensajes("lean")