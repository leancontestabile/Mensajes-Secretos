from tkinter import *

def interfaz_login():
    raiz_login = Tk()
    raiz_login.title("Inicio de sesion")
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

    boton_ingresar = Button(frame_botones,text="Ingresar",bg="#D5CF13", command=lambda: boton_ingreso(input_usuario,input_contraseña))
    boton_ingresar.grid(row=0,column=1, padx=5)

    raiz_login.mainloop()
