# Todos los objetivos integrados en un solo archivo para el segundo video.

import doctest
from os import remove
from os import rename



from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    
    usuario_existente = False
    usuario_insertado = False
    
    if usuario_valido and clave_valida:

        archivo_usuarios=open("usuario_clave.csv") 
        nuevo_archivo_usuarios =open("nuevo_usuario_clave.csv","w")

        usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)

        while usuario_archivo != "":

            if usuario_archivo == usuario:
                usuario_existente = True
                nuevo_archivo_usuarios.write(f"{usuario_archivo},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos}\n")
            elif usuario < usuario_archivo and not usuario_existente and not usuario_insertado:
                usuario_insertado = True

                nuevo_archivo_usuarios.write(f"{usuario},{clave},{id_pregunta_seguridad},{respuesta},0\n")
                nuevo_archivo_usuarios.write(f"{usuario_archivo},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos}\n")
                messagebox.showinfo("completado","Identificador guardado")
            else:
                nuevo_archivo_usuarios.write(f"{usuario_archivo},{clave_archivo},{id_pregunta_seguridad_archivo},{respuesta_archivo},{intentos}\n")
                
            usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)
            
            if usuario_archivo == "":
                if not usuario_existente and not usuario_insertado:
                    usuario_insertado = True
                    nuevo_archivo_usuarios.write(f"{usuario},{clave},{id_pregunta_seguridad},{respuesta},0\n")
                    messagebox.showinfo("completado","Identificador guardado")
                elif not usuario_insertado and usuario_existente:
                    messagebox.showwarning("error","Identificador en uso")
    elif not usuario_valido or not clave_valida:
        messagebox.showwarning("eror","clave o usuario invalidos")

        archivo_usuarios.close()
        nuevo_archivo_usuarios.close()
        remove("usuario_clave.csv")
        rename("nuevo_usuario_clave.csv","usuario_clave.csv")

    return usuario_insertado

        

                
def comprobar_usuario_clave_correctos(usuario,clave):

    archivo = open("usuario_clave.csv")
    usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo)
    encontrado = False

    while usuario_archivo != "" and not encontrado:

        if usuario == usuario_archivo:
            if clave == clave_archivo:
                encontrado = True

        usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo)
        
    return encontrado


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

    messagebox.showwarning("advertencia","Respuesta incorrecta")

    remove("usuario_clave.csv")
    rename("nuevo_usuario_clave.csv","usuario_clave.csv")



def recuperar_contraseña(usuario,id_pregunta,respuesta_pregunta):

    INTENTOS_MAXIMOS = 3
    encontrado = False

    archivo_usuarios = open("usuario_clave.csv")
    usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)
    
    
    while usuario_archivo != "" and not encontrado:

            if  usuario == usuario_archivo:
                encontrado = True
                if id_pregunta == id_pregunta_seguridad_archivo:
                    if int(intentos) < INTENTOS_MAXIMOS:
                        if respuesta_pregunta == respuesta_archivo:
                            messagebox.showinfo("completado",f"usuario:{usuario_archivo} clave:{clave_archivo}")
                            archivo_usuarios.close()
                        else:
                            archivo_usuarios.close()
                            intentos_actualizado = str(int(intentos)+1)
                            actualizar_intentos(usuario,intentos_actualizado)                    
                    else:
                        messagebox.showerror("error","Usuario bloqueado")
                        archivo_usuarios.close()    
                """elif usuario_archivo == "":
                messagebox.showerror("error","Usuario no encontrado")
                archivo_usuarios.close()   """
            else:
                usuario_archivo,clave_archivo,id_pregunta_seguridad_archivo,respuesta_archivo,intentos = leer_usuario(archivo_usuarios)
                if usuario_archivo == "":
                    messagebox.showerror("error","Usuario no encontrado")
                    archivo_usuarios.close()  

            


# objetivo 1: cifrado cesar
def normalizar_mensaje(mensaje):
    """recibe un mensaje y convierte las vocales tildadas en vocales sin tildar y las "ñ" en "ni", el resto de caracteres los deja igual"""
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
    """
    recibe un mensaje , en caso de ser una letra o numero se "desplaza" una cantidad de veces a la derecha definido por el valor de clave,
    en caso de ser un simbolo o espacio lo deja igual. para descifrar el mensaje se introduce una clave negativa
    
    funcion hecha por Conde Brian Agustin
    
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

#Funciones para integrar el Objetivo 1 con la interfaz gráfica del Objetivo 3.

def boton_cifrado_cesar(inputMensaje, inputClave, resultado_text):
    """
    La función recibe 3 parámetros que son variables contenidas en la interfaz gráfica, a las dos primeras se les aplica el método get() 
    para conseguir la información de los cuadros de texto (Entry), y luego se invoca a la función del objetivo 1 para cifrar el mensaje ingresado 
    con su clave correspondiente, que se muestra en la interfaz utilizando la última variable ingresada como parámetro (otro Label).
    
    Mutazzi Nicolás Rocco
    """
    mensaje = inputMensaje.get()
    clave = int(inputClave.get())
    mensaje_cifrado = cifrado_cesar(mensaje, clave)
    mostrar_resultado(resultado_text, "Texto cifrado (Cesar):", mensaje_cifrado)

def boton_descifrado_cesar(inputMensaje, inputClave, resultado_text):
    """
    Lo mismo que la función del botón de cifrado, solamente que ahora se utiliza la clave negativa, para descifrar en vez de cifrar.
    
    Mutazzi Nicolás Rocco
    """
    mensaje = inputMensaje.get()
    clave = int(inputClave.get())
    mensaje_descifrado = cifrado_cesar(mensaje, -clave)
    mostrar_resultado(resultado_text, "Texto descifrado (Cesar):", mensaje_descifrado)



def boton_ingreso(raiz,input_usuario, input_clave):
    usuario = input_usuario.get()
    clave = input_clave.get()

    if comprobar_usuario_clave_correctos(usuario,clave):
        raiz.destroy()
        interfaz_mensajes()
    else: 
        messagebox.showwarning("Identificador inexistente o clave errónea","Si no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el botón recuperar clave")
        

def cargar_preguntas():
    lista = []

    archivo_preguntas=open("preguntas.csv")
    num_pregunta,pregunta =leer_preguntas(archivo_preguntas)

    while num_pregunta != "":
        lista.append(f" {num_pregunta}-{pregunta}")
        num_pregunta,pregunta =leer_preguntas(archivo_preguntas)
    
    return lista



def boton_registro(raiz):
    raiz.destroy()
    lista_preguntas = cargar_preguntas()
    interfaz_registro(lista_preguntas)

def boton_recuperacion_contraseña(raiz):
    raiz.destroy()
    lista_preguntas = cargar_preguntas()
    interfaz_recuperacion_contraseña(lista_preguntas)


def boton_recuperar_contraseña(input_usuario,combo_var,input_respuesta):
    usuario = input_usuario.get()
    id_pregunta_seguridad = combo_var.get().split("-")[0]
    respuesta = input_respuesta.get()

    recuperar_contraseña(usuario,id_pregunta_seguridad,respuesta)


def boton_ingresar_registro(raiz,input_usuario,input_contraseña,combo_var,input_respuesta):

    usuario = input_usuario.get()
    clave= input_contraseña.get()
    id_pregunta_seguridad = combo_var.get().split("-")[0]
    respuesta = input_respuesta.get()
    
    usuario_insertado = crear_usuario(usuario,clave,id_pregunta_seguridad, respuesta)
    
    if usuario_insertado:
        raiz.destroy()
        interfaz_login()



# objetivo 2: cifrado atbash
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
    letras_minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letras_invertidas_mayuscula = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "Ñ", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
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
    print(doctest.testmod())

main()

# objetivo 3: interfaz grafica de usuario


mensaje_cifrado_global = "" #Variable global

def boton_interfaz_login(raiz):
    raiz.destroy()
    interfaz_login()


def interfaz_inicial():
    raiz = Tk()
    raiz.title('TP Grupal Parte 1 - Grupo: Argentina') 
    raiz.resizable(0,0)
    raiz.geometry("900x600")
    raiz.config(bg="#9ED8F9")

    mi_frame = Frame(raiz,bg="#9ED8F9")
    mi_frame.config(bd=10,relief="groove")
    mi_frame.pack(pady=100)

    label_bienvenida = Label(mi_frame,font=('Courier',12),bg="#9ED8F9",text="Bienvenido a la aplicación de mensajes secretos del grupo Argentina. \n Para ingresar presione ingresar, para crear una nueva cuenta presione registrar")
    label_bienvenida.grid(row=0,column=0,padx=10,pady=10, columnspan=2)

    boton_continuar = Button(mi_frame,text="Ingresar",bg="#D5CF13",command=lambda:boton_interfaz_login(raiz))
    boton_continuar.grid(row=1,column=0,pady=10,padx=(250, 5))

    boton_registrar = Button(mi_frame,text="Registrar",bg="#D5CF13", command=lambda: boton_registro(raiz))
    boton_registrar.grid(row=1,column=1, pady=10, padx=(5, 250))

    label_integrantes = Label(mi_frame,font=('Courier',12),bg="#9ED8F9",text="Construída por:\n \n Tomás Ghiglione \n Nicolás Mutazzi \n Matías Gonzalez Vieyra \n Brian Agustín Conde \n Leandro Contestabile")
    label_integrantes.grid(row=2,column=0,pady=10,columnspan=2)

    raiz.mainloop()

def interfaz_login():
    raiz_login = Tk()
    raiz_login.title("Identificacion para acceso")
    raiz_login.resizable(0,0)
    raiz_login.geometry("750x500")
    raiz_login.config(bg="#9ED8F9")
    frame_login = Frame(raiz_login,bg="#9ED8F9")
    frame_login.config(bd=10,relief="groove")
    frame_login.pack(pady=100)

    label_usuario = Label(frame_login,font=('Courier',12),bg="#9ED8F9",text="Usuario:")
    label_usuario.grid(row=0,column=0,padx=5,pady=10)
    
    label_contraseña = Label(frame_login,font=('Courier',12),bg="#9ED8F9",text="Contraseña:")
    label_contraseña.grid(row=1,column=0,padx=5,pady=10)
    
    input_usuario=Entry(frame_login)
    input_usuario.grid(row=0,column=1,padx=10)
    
    input_contraseña=Entry(frame_login)
    input_contraseña.grid(row=1,column=1,padx=10)

    frame_botones = Frame(raiz_login, bg="#9ED8F9")
    frame_botones.pack(pady=15)

    boton_ingresar = Button(frame_botones,text="Ingresar",bg="#D5CF13", command=lambda: boton_ingreso(raiz_login,input_usuario,input_contraseña))
    boton_ingresar.grid(row=0,column=0, padx=5)


    boton_recuperar = Button(frame_botones,text="Recuperar",bg="#D5CF13", command=lambda: boton_recuperacion_contraseña(raiz_login))
    boton_recuperar.grid(row=0,column=2, padx=5)
    
    
    raiz_login.mainloop()

def interfaz_registro(lista_preguntas):

    raiz = Tk()
    raiz.title("Registro")
    raiz.resizable(0,0)
    raiz.geometry("750x500")
    raiz.config(bg="#9ED8F9")
    frame_registro = Frame(raiz,bg="#9ED8F9")
    frame_registro.config(bd=10,relief="groove")
    frame_registro.pack(pady=100)

    label_usuario = Label(frame_registro,font=('Courier',12),bg="#9ED8F9",text="Usuario:")
    label_usuario.grid(row=0,column=0,padx=5,pady=10)
    
    label_contraseña = Label(frame_registro,font=('Courier',12),bg="#9ED8F9",text="Contraseña:")
    label_contraseña.grid(row=1,column=0,padx=5,pady=10)

    label_pregunta = Label(frame_registro,font=('Courier',12),bg="#9ED8F9",text="Pregunta de seguridad:")
    label_pregunta.grid(row=2,column=0,padx=5,pady=10)

    label_respuesta = Label(frame_registro,font=('Courier',12),bg="#9ED8F9",text="Respuesta:")
    label_respuesta.grid(row=3,column=0,padx=5,pady=10)
    
    input_usuario=Entry(frame_registro)
    input_usuario.grid(row=0,column=1,padx=10)
    
    input_contraseña=Entry(frame_registro)
    input_contraseña.grid(row=1,column=1,padx=10)

    combo_var = tk.StringVar()
    combobox = ttk.Combobox(frame_registro, textvariable=combo_var,values=lista_preguntas)
    combobox.grid(row=2,column=1,padx=10)

    input_respuesta=Entry(frame_registro)
    input_respuesta.grid(row=3,column=1,padx=10)

    frame_botones = Frame(raiz, bg="#9ED8F9")
    frame_botones.pack(pady=15)

    boton_ingresar = Button(frame_botones,text="Ingresar",bg="#D5CF13", command=lambda: boton_ingresar_registro(raiz,input_usuario,input_contraseña,combo_var,input_respuesta))
    boton_ingresar.grid(row=0,column=1, padx=5)


def interfaz_recuperacion_contraseña(lista_preguntas):
    raiz = Tk()
    raiz.title("Recuperacion Clave")
    raiz.resizable(0,0)
    raiz.geometry("750x500")
    raiz.config(bg="#9ED8F9")
    frame_recuperar = Frame(raiz,bg="#9ED8F9")
    frame_recuperar.config(bd=10,relief="groove")
    frame_recuperar.pack(pady=100)

    label_usuario = Label(frame_recuperar,font=('Courier',12),bg="#9ED8F9",text="Usuario:")
    label_usuario.grid(row=0,column=0,padx=5,pady=10)
    
    label_pregunta = Label(frame_recuperar,font=('Courier',12),bg="#9ED8F9",text="Pregunta de seguridad:")
    label_pregunta.grid(row=2,column=0,padx=5,pady=10)

    label_respuesta = Label(frame_recuperar,font=('Courier',12),bg="#9ED8F9",text="Respuesta:")
    label_respuesta.grid(row=3,column=0,padx=5,pady=10)
    
    input_usuario=Entry(frame_recuperar)
    input_usuario.grid(row=0,column=1,padx=10)

    combo_var = tk.StringVar()
    combobox = ttk.Combobox(frame_recuperar, textvariable=combo_var,values=lista_preguntas)
    combobox.grid(row=2,column=1,padx=10)

    input_respuesta=Entry(frame_recuperar)
    input_respuesta.grid(row=3,column=1,padx=10)

    frame_botones = Frame(raiz, bg="#9ED8F9")
    frame_botones.pack(pady=15)

    boton_recuperar = Button(frame_botones,text="recuperar",bg="#D5CF13", command=lambda: boton_recuperar_contraseña(input_usuario,combo_var,input_respuesta))
    boton_recuperar.grid(row=0,column=1, padx=5)



def cifrar_atbash(texto):
    texto_cifrado = cifrado_atbash(texto) 
    return texto_cifrado

def cifrar(inputMensaje, resultado_text):
    global mensaje_cifrado_global 
    mensaje = inputMensaje.get()
    mensaje_cifrado = cifrar_atbash(mensaje)
    mensaje_cifrado_global = mensaje_cifrado 
    mostrar_resultado(resultado_text, "Texto cifrado (Atbash):", mensaje_cifrado)


def interfaz_mensajes():
    raiz = Tk()
    raiz.title('TP Grupal Parte 1 - Grupo: Argentina') 
    raiz.resizable(0,0)
    raiz.geometry("750x500")
    raiz.config(bg="#9ED8F9")

    mi_frame = Frame(raiz,bg="#9ED8F9")
    mi_frame.config(bd=10,relief="groove")
    mi_frame.pack(pady=(100, 0))

    label_mensaje = Label(mi_frame,font=('Courier',12),bg="#9ED8F9",text="Ingrese mensaje:")
    label_mensaje.grid(row=0,column=0,padx=5,pady=10)
    
    label_clave = Label(mi_frame,font=('Courier',12),bg="#9ED8F9",text="Ingrese Clave en caso de César:")
    label_clave.grid(row=1,column=0,padx=5,pady=10)
    
    input_mensaje=Entry(mi_frame)
    input_mensaje.grid(row=0,column=1,padx=10)
    
    input_clave=Entry(mi_frame)
    input_clave.grid(row=1,column=1,padx=10)

    frame_botones = Frame(raiz, bg="#9ED8F9")
    frame_botones.pack(pady=15)
    
    boton_cifrar_cesar = Button(frame_botones,text="Cifrar César", bg="#D5CF13", command=lambda: boton_cifrado_cesar(input_mensaje,input_clave, resultado_text))
    boton_cifrar_cesar.grid(row=0,column=0, padx=5)
    
    boton_descifrar_cesar = Button(frame_botones,text="Descifrar César",bg="#D5CF13", command=lambda: boton_descifrado_cesar(input_mensaje,input_clave, resultado_text))
    boton_descifrar_cesar.grid(row=0,column=1, padx=5)
    
    resultado_text = Text(mi_frame, font=('Courier', 12), bg="white", height=5, width=40, state=DISABLED)
    resultado_text.grid(row=2, column=0, padx=5, pady=10)

    boton_cifrar_atbash = Button(frame_botones,text="Cifrar Atbash",bg="#D5CF13", command=lambda: cifrar(input_mensaje, resultado_text))
    boton_cifrar_atbash.grid(row=0,column=2, padx=5)
    
    boton_descifrar_atbash = Button(frame_botones,text="Descifrar Atbash",bg="#D5CF13", command=lambda: cifrar(input_mensaje, resultado_text))
    boton_descifrar_atbash.grid(row=0,column=3, padx=5)

    raiz.mainloop()

def mostrar_resultado(texto_cuadro, titulo, texto):
    """ Muestra los mensajes cifrados y descifrados en un cuadro.
        Matias Gonzalez.
    """
    texto_cuadro.config(state=NORMAL)
    texto_cuadro.delete(1.0, END)
    texto_cuadro.insert(INSERT, titulo)
    texto_cuadro.insert(INSERT, "\n")
    texto_cuadro.insert(INSERT, texto)
    texto_cuadro.config(state=DISABLED)



interfaz_inicial()


