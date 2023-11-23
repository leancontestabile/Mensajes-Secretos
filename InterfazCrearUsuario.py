from tkinter import *

# Interfaz Crear Usuario, Objetivo 1 - TP parte 2.

def interfazInicial():
    raiz = Tk()
    raiz.title('TP Grupal Parte 1 - Grupo: Argentina') 
    raiz.resizable(True, True)
    raiz.geometry("1024x768")
    raiz.iconbitmap("argentina.ico")
    raiz.config(bg="#9ED8F9")

    miFrame = Frame(raiz,bg="#9ED8F9")
    miFrame.config(bd=10,relief="groove")
    miFrame.pack(pady=100)

    labelBienvenida = Label(miFrame,font=('Courier',12),bg="#9ED8F9",text="Bienvenido a la aplicación de mensajes secretos del grupo Argentina. \n Es necesario que se registre previamente antes de usar la app.")
    labelBienvenida.grid(row=0,column=0,padx=10,pady=10)

    botonCrearUsuario = Button(miFrame,font=('Arial',10),text="Crear Usuario",bg="#856ff8", bd=4 ,command=interfazCrearUsuario)
    botonCrearUsuario.grid(row=1,column=0,pady=10)

    botonIngresoUsuario = Button(miFrame,font=('Arial',10),text="Ingreso Usuario",bg="#856ff8", bd=4 ,command=interfazIngresoUsuario)
    botonIngresoUsuario.grid(row=2,column=0,pady=10)

    labelIntegrantes = Label(miFrame,font=('Courier',12),bg="#9ED8F9",text="Construída por:\n Matías Gonzalez Vieyra \n Brian Agustín Conde \n Leandro Contestabile")
    labelIntegrantes.grid(row=3,column=0,pady=10)

    raiz.mainloop()


def interfazCrearUsuario():
    """ Brian Conde, Matias Gonzalez"""
    raiz = Tk()
    raiz.title('Crear Usuario') 
    raiz.resizable(True, True)
    raiz.geometry("1024x768")
    raiz.iconbitmap("argentina.ico")
    raiz.config(bg="#9ED8F9")

    miFrame = Frame(raiz,bg="#9ED8F9")
    miFrame.config(bd=10,relief="groove")
    miFrame.pack(pady=(100, 0))

    nuevoUsuario = Label(miFrame,font=('Arial',12),bg="#9ED8F9",text="Ingrese un nombre de usuario:")
    nuevoUsuario.grid(row=0,column=0,padx=5,pady=10)

    inputNuevoUsuario=Entry(miFrame, bd=7)
    inputNuevoUsuario.grid(row=0,column=1,padx=10)
    
    nuevaClave = Label(miFrame,font=('Arial',12),bg="#9ED8F9",text="Ingrese una clave:")
    nuevaClave.grid(row=1,column=0,padx=5,pady=10)

    inputNuevaClave=Entry(miFrame, bd=7)
    inputNuevaClave.grid(row=1,column=1,padx=10)

    recuperarClave = Label(miFrame,font=('Arial',12),bg="#9ED8F9",text="Ciudad preferida?:")
    recuperarClave.grid(row=2,column=0,padx=5,pady=10)

    inputRecuperarClave=Entry(miFrame, bd=7)
    inputRecuperarClave.grid(row=2,column=1,padx=10)

    botonRegistrar= Button(miFrame,font=('Arial',10),text="Registrar",bg="#856ff8", bd=4 , cursor="hand2",command=interfazInicial)
    botonRegistrar.grid(row=4,column=0,pady=10)

    raiz.mainloop()


def interfazIngresoUsuario():
    """ Brian Conde, Matias Gonzalez"""
    raiz = Tk()
    raiz.title('Ingreso Usuario') 
    raiz.resizable(True, True)
    raiz.geometry("1024x768")
    raiz.iconbitmap("argentina.ico")
    raiz.config(bg="#9ED8F9")

    miFrame = Frame(raiz,bg="#9ED8F9")
    miFrame.config(bd=10,relief="groove")
    miFrame.pack(pady=(100, 0))

    raiz.mainloop()


interfazInicial()
