from os import remove
from os import rename


def verificar_longitud(minimo,maximo,longitud):

    if minimo <= longitud <= maximo:
        longitud_valida = True
    else:
        longitud_valida = False
    return longitud_valida

def validar_usuario(usuario):
    caracteres_validos = ["_","-","."]
    LONGITUD_MINIMA = 5
    LONGITUD_MAXIMA = 15
    usuario_valido = True
    longitud_usuario = len(usuario)

    longitud_valida = verificar_longitud(LONGITUD_MINIMA,LONGITUD_MAXIMA,longitud_usuario)

    if longitud_valida: 
        i = 0
        while usuario_valido and i < longitud_usuario:
            if usuario[i].isalnum():
                pass
            elif usuario[i] in caracteres_validos:
                pass
            else:
                usuario_valido = False
            i+=1
    
    return usuario_valido

def validar_clave(clave):

    caracteres_pedidos = ["-","#","*"]

    LONGITUD_MINIMA = 4
    LONGITUD_MAXIMA = 8

    longitud_clave = len(clave)

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_pedido = False
    adyacente = False

    longitud_valida = verificar_longitud(LONGITUD_MINIMA,LONGITUD_MAXIMA,longitud_clave)
    
    if longitud_valida:
        i=0
        caracter_anterior = ""
        while not adyacente and i < longitud_clave:
            if clave[i] == caracter_anterior:
                adyacente = True
            elif clave[i].isalpha():
                if clave[i].islower():
                    tiene_minuscula = True
                else:
                    tiene_mayuscula = True
            elif clave[i].isnumeric():
                tiene_numero = True
            elif clave[i] in caracteres_pedidos:
                tiene_caracter_pedido = True
            caracter_anterior = clave[i]
            i+=1
        
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_pedido and not adyacente

def leer_usuario(archivo):
    linea = archivo.readline()

    if linea:   
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = "","","","",""

    return devolver

def leer_preguntas(archivo):
    linea = archivo.readline()

    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = "",""
    return devolver


def crear_usuario(usuario,clave,id_pregunta_seguridad, respuesta):

    usuario_valido = validar_usuario(usuario)
    clave_valida = validar_clave(clave)
    

    if usuario_valido and clave_valida:

        archivo_usuarios = open("usuario_clave.csv")
        nuevo_archivo_usuarios = open("nuevo_usuario_clave.csv","w")

        usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)

        usuario_existente = False
        usuario_insertado = False

        while usuario_archivo != "":

            if usuario_archivo == usuario:
                usuario_existente = True
                nuevo_archivo_usuarios.write(f"{usuario_archivo},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos}\n")
            elif usuario < usuario_archivo and not usuario_existente and not usuario_insertado:
                usuario_insertado = True

                nuevo_archivo_usuarios.write(f"{usuario},{clave},{id_pregunta_seguridad},{respuesta},0\n")
                nuevo_archivo_usuarios.write(f"{usuario_archivo},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos}\n")
                print("Identificador guardado")
            else:
                nuevo_archivo_usuarios.write(f"{usuario_archivo},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos}\n")
            
            usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)
        
        if usuario_archivo == "":
            if not usuario_existente and not usuario_insertado:
                nuevo_archivo_usuarios.write(f"{usuario},{clave},{id_pregunta_seguridad},{respuesta},0\n")
                print("Identificador guardado")
            elif not usuario_insertado and usuario_existente:
                print("Identificador en uso")

        archivo_usuarios.close()
        nuevo_archivo_usuarios.close()

        remove("usuario_clave.csv")
        rename("nuevo_usuario_clave.csv","usuario_clave.csv")

                
def comprobar_usuario_clave_correctos(usuario,clave):
    with open("usuario_clave.csv") as archivo_usuario_clave:

        usuario_archivo,clave_archivo = leer_usuario(archivo_usuario_clave)

        usuario_encontrado = False
        clave_correcta = False

        while not usuario_encontrado and usuario_encontrado != "":

            if usuario == usuario_archivo:

                usuario_encontrado = True
                if clave == clave_archivo:
                    clave_correcta = True
                    
            usuario_archivo,clave_archivo = leer_usuario(archivo_usuario_clave)
        
        if not usuario_encontrado or not clave_correcta:
            print("Identificador inexistente o clave errónea")
            print("Si no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el botón recuperar clave")



def actualizar_intentos(usuario,intentos_actualizado):

    archivo_usuarios = open("usuario_clave.csv")
    nuevo_archivo_usuarios = open("nuevo_usuario_clave.csv","w")

    usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)

    
    while usuario_archivo != "":

        if usuario_archivo == usuario:
            nuevo_archivo_usuarios.write(f"{usuario},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos_actualizado}\n")
        else:
            nuevo_archivo_usuarios.write(f"{usuario_archivo},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos}\n")

        usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)
    
    
    
    archivo_usuarios.close()
    nuevo_archivo_usuarios.close()

    print("Respuesta incorrecta")

    remove("usuario_clave.csv")
    rename("nuevo_usuario_clave.csv","usuario_clave.csv")



def recuperar_contraseña(usuario,id_pregunta,respuesta_pregunta):

    INTENTOS_MAXIMOS = 3
    archivo_usuarios = open("usuario_clave.csv")

    usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)
    
    actualizdo = False
    while usuario_archivo != usuario and usuario_archivo != "":
        
        while id_pregunta_seguridad_archivo != "" and not actualizdo:

            if id_pregunta == id_pregunta_seguridad_archivo and usuario == usuario_archivo and not actualizdo:

                
                if int(intentos) < INTENTOS_MAXIMOS:
                    if respuesta_pregunta == respuesta_archivo:
                        print(f"usuario:{usuario_archivo} clave:{clave_archivo}")
                    else:
                        archivo_usuarios.close()
                        intentos_actualizado = str(int(intentos)+1)
                        actualizar_intentos(usuario,intentos_actualizado)
                                    
                else:
                    print("Usuario bloqueado")
                        
                if usuario_archivo == "":
                    print("Usuario no encontrado")

                actualizdo = True

            else:
                usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)

    


crear_usuario("hoLa12","Chau-23",3,"no se")
crear_usuario("poLa12","Chau-23",3,"no se")
crear_usuario("xoLa12","Chau-23",3,"no se")
crear_usuario("AoLa12","Chau-23",3,"no se")


recuperar_contraseña("hoLa12","3","no se")