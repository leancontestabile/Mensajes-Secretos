from cifradoatbash import cifrado_atbash
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

    botonCifrarCesar = Button(frameBotones,text="Cifrar César", bg="#D5CF13")
    botonCifrarCesar.grid(row=0,column=0, padx=5)
    
    botonDescifrarCesar = Button(frameBotones,text="Descifrar César",bg="#D5CF13")
    botonDescifrarCesar.grid(row=0,column=1, padx=5)
    
    resultado_text = Text(miFrame, font=('Courier', 12), bg="white", height=5, width=40, state=DISABLED)
    resultado_text.grid(row=2, column=0, padx=5, pady=10)

    botonCifrarAtbash = Button(frameBotones,text="Cifrar Atbash",bg="#D5CF13", command=lambda: cifrar(inputMensaje, resultado_text))
    botonCifrarAtbash.grid(row=0,column=2, padx=5)
    
    botonDescifrarAtbash = Button(frameBotones,text="Descifrar Atbash",bg="#D5CF13", command=lambda: descifrar(inputMensaje, resultado_text))
    botonDescifrarAtbash.grid(row=0,column=3, padx=5)

    raiz.mainloop()

def mostrar_resultado(texto_cuadro, titulo, texto):
    texto_cuadro.config(state=NORMAL)
    texto_cuadro.delete(1.0, END)
    texto_cuadro.insert(INSERT, titulo)
    texto_cuadro.insert(INSERT, "\n")
    texto_cuadro.insert(INSERT, texto)
    texto_cuadro.config(state=DISABLED)

interfazInicial()




