from tkinter import *

def interfazConsulta(mensajes, cantidad):
    raiz = Tk()
    raiz.title('TP Grupal Parte 2 - Grupo: Argentina') 
    raiz.resizable(0, 0)
    raiz.geometry("750x500")
    raiz.iconbitmap("argentina.ico")
    raiz.config(bg="#9ED8F9")
    
    miFrame = Frame(raiz, bg="#9ED8F9")
    miFrame.config(bd=10, relief="groove")
    miFrame.pack(pady=100)
    
    labelLista = Label(miFrame, font=('Courier', 12), bg="#9ED8F9", text="Lista de mensajes:")
    labelLista.grid(row=0, column=0, padx=10, pady=10)
    
    lista = Listbox(miFrame, width=50, height=10)
    lista.grid(row=1, column=0, padx=10, pady=10)
    
    for mensaje in mensajes:
        lista.insert(END, mensaje)

    labelTotal = Label(miFrame, font=('Courier', 12), bg="#9ED8F9", text=f"Total de mensajes: {cantidad}")
    labelTotal.grid(row=2, column=0, padx=10, pady=10)
    
    raiz.mainloop()

#interfazConsulta(["Mensaje 1", "Mensaje 2", "Mensaje 3", "Mensaje 4"], 10)