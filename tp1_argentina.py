# Todos los objetivos integrados en un solo archivo para el segundo video.

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
    import doctest
    print(doctest.testmod())

main()

# objetivo 3: interfaz grafica de usuario
from tkinter import *

mensaje_cifrado_global = "" #Variable global

def interfazInicial():
    raiz = Tk()
    raiz.title('TP Grupal Parte 1 - Grupo: Argentina') 
    raiz.resizable(0,0)
    raiz.geometry("750x500")
    raiz.iconbitmap("argentina.ico")
    raiz.config(bg="#9ED8F9")

    miFrame = Frame(raiz,bg="#9ED8F9")
    miFrame.config(bd=10,relief="groove")
    miFrame.pack(pady=100)

    labelBienvenida = Label(miFrame,font=('Courier',12),bg="#9ED8F9",text="Bienvenido a la aplicación de mensajes secretos del grupo Argentina. \n Para continuar presione continuar, de lo contrario cierre la ventana")
    labelBienvenida.grid(row=0,column=0,padx=10,pady=10)

    botonContinuar = Button(miFrame,text="Continuar",bg="#D5CF13",command=interfazContinuar)
    botonContinuar.grid(row=1,column=0,pady=10)

    labelIntegrantes = Label(miFrame,font=('Courier',12),bg="#9ED8F9",text="Construída por:\n \n Tomás Ghiglione \n Nicolás Mutazzi \n Matías Gonzalez Vieyra \n Brian Agustín Conde \n Leandro Contestabile")
    labelIntegrantes.grid(row=2,column=0,pady=10)

    raiz.mainloop()

def cifrar_atbash(texto):
    texto_cifrado = cifrado_atbash(texto) 
    return texto_cifrado

def cifrar(inputMensaje, resultado_text):
    global mensaje_cifrado_global 
    mensaje = inputMensaje.get()
    mensaje_cifrado = cifrar_atbash(mensaje)
    mensaje_cifrado_global = mensaje_cifrado 
    mostrar_resultado(resultado_text, "Texto cifrado (Atbash):", mensaje_cifrado)

def descifrar(inputMensaje, resultado_text):
    global mensaje_cifrado_global  
    mensaje_descifrado = cifrar_atbash(mensaje_cifrado_global) 
    mostrar_resultado(resultado_text, "Texto descifrado (Atbash):", mensaje_descifrado)

def interfazContinuar():
    raiz = Tk()
    raiz.title('TP Grupal Parte 1 - Grupo: Argentina') 
    raiz.resizable(0,0)
    raiz.geometry("750x500")
    raiz.iconbitmap("argentina.ico")
    raiz.config(bg="#9ED8F9")

    miFrame = Frame(raiz,bg="#9ED8F9")
    miFrame.config(bd=10,relief="groove")
    miFrame.pack(pady=(100, 0))

    labelMensaje = Label(miFrame,font=('Courier',12),bg="#9ED8F9",text="Ingrese mensaje:")
    labelMensaje.grid(row=0,column=0,padx=5,pady=10)
    
    labelClave = Label(miFrame,font=('Courier',12),bg="#9ED8F9",text="Ingrese Clave en caso de César:")
    labelClave.grid(row=1,column=0,padx=5,pady=10)
    
    inputMensaje=Entry(miFrame)
    inputMensaje.grid(row=0,column=1,padx=10)
    
    inputClave=Entry(miFrame)
    inputClave.grid(row=1,column=1,padx=10)

    frameBotones = Frame(raiz, bg="#9ED8F9")
    frameBotones.pack(pady=15)
    
    botonCifrarCesar = Button(frameBotones,text="Cifrar César", bg="#D5CF13", command=lambda: boton_cifrado_cesar(inputMensaje,inputClave, resultado_text))
    botonCifrarCesar.grid(row=0,column=0, padx=5)
    
    botonDescifrarCesar = Button(frameBotones,text="Descifrar César",bg="#D5CF13", command=lambda: boton_descifrado_cesar(inputMensaje,inputClave, resultado_text))
    botonDescifrarCesar.grid(row=0,column=1, padx=5)
    
    resultado_text = Text(miFrame, font=('Courier', 12), bg="white", height=5, width=40, state=DISABLED)
    resultado_text.grid(row=2, column=0, padx=5, pady=10)

    botonCifrarAtbash = Button(frameBotones,text="Cifrar Atbash",bg="#D5CF13", command=lambda: cifrar(inputMensaje, resultado_text))
    botonCifrarAtbash.grid(row=0,column=2, padx=5)
    
    botonDescifrarAtbash = Button(frameBotones,text="Descifrar Atbash",bg="#D5CF13", command=lambda: descifrar(inputMensaje, resultado_text))
    botonDescifrarAtbash.grid(row=0,column=3, padx=5)

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

interfazInicial()
