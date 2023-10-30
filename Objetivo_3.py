from tkinter import *
from Integración import boton_cifrado_cesar, boton_descifrado_cesar 

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

    cifrado = Label(miFrame,font=('Courier',12), bg="#9ED8F9", text="")
    cifrado.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    descifrado = Label(miFrame,font=('Courier',12), bg="#9ED8F9", text="")
    descifrado.grid(row=2, column=0, columnspan=2, padx=5, pady=10) 
    
    inputMensaje=Entry(miFrame)
    inputMensaje.grid(row=0,column=1,padx=10)
    
    inputClave=Entry(miFrame)
    inputClave.grid(row=1,column=1,padx=10)

    frameBotones = Frame(raiz, bg="#9ED8F9")
    frameBotones.pack(pady=15)

    botonCifrarCesar = Button(frameBotones,text="Cifrar César", bg="#D5CF13", command=lambda: boton_cifrado_cesar(inputMensaje, inputClave, cifrado))
    botonCifrarCesar.grid(row=0,column=0, padx=5)
    
    botonDescifrarCesar = Button(frameBotones,text="Descifrar César",bg="#D5CF13", command:lambda: boton_descifrado_cesar(inputMensaje, inputClave, descifrado))
    botonDescifrarCesar.grid(row=0,column=1, padx=5)
    
    botonCifrarAtbash = Button(frameBotones,text="Cifrar Atbash",bg="#D5CF13")
    botonCifrarAtbash.grid(row=0,column=2, padx=5)
    
    botonDescifrarAtbash = Button(frameBotones,text="Descifrar Atbash",bg="#D5CF13")
    botonDescifrarAtbash.grid(row=0,column=3, padx=5)
    
    raiz.mainloop()

interfazInicial()
