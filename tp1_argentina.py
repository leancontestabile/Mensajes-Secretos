# Todos los objetivos integrados en un solo archivo para el segundo video.

# objetivo 1: cifrado cesar

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

class AtBashMensaje: # sin variable global
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('TP Grupal Parte 1 - Grupo: Argentina') 
        self.raiz.resizable(0,0)
        self.raiz.geometry("750x500")
        self.raiz.iconbitmap("argentina.ico")
        self.raiz.config(bg="#9ED8F9")
        
        self.mensaje_cifrado = ""

        self.miFrame = Frame(self.raiz,bg="#9ED8F9")
        self.miFrame.config(bd=10,relief="groove")
        self.miFrame.pack(pady=100)

        labelBienvenida = Label(self.miFrame, font=('Courier', 12), bg="#9ED8F9", text="Bienvenido a la aplicación de mensajes secretos del grupo Argentina. \n Para continuar presione continuar, de lo contrario cierre la ventana")
        labelBienvenida.grid(row=0, column=0, padx=10, pady=10)

        botonContinuar = Button(self.miFrame, text="Continuar", bg="#D5CF13", command=self.interfazContinuar)
        botonContinuar.grid(row=1, column=0, pady=10)

        labelIntegrantes = Label(self.miFrame, font=('Courier', 12), bg="#9ED8F9", text="Construída por:\n \n Tomás Ghiglione \n Nicolás Mutazzi \n Matías Gonzalez Vieyra \n Brian Agustín Conde \n Leandro Contestabile")
        labelIntegrantes.grid(row=2, column=0, pady=10)

    def cifrar_atbash(self, texto):
        return cifrado_atbash(texto)

    def cifrar(self, inputMensaje, resultado_text):
        mensaje = inputMensaje.get()
        mensaje_cifrado = self.cifrar_atbash(mensaje)
        self.mensaje_cifrado = mensaje_cifrado
        self.mostrar_resultado(resultado_text, "Texto cifrado (Atbash):", mensaje_cifrado)

    def descifrar(self, resultado_text):
        if self.mensaje_cifrado:
            mensaje_descifrado = self.cifrar_atbash(self.mensaje_cifrado)
            self.mostrar_resultado(resultado_text, "Texto descifrado (Atbash):", mensaje_descifrado)
        else:
            self.mostrar_resultado(resultado_text, "No hay mensaje cifrado para descifrar.", "")

    def interfazContinuar(self):
        self.miFrame.destroy()
        
        self.miFrame = Frame(self.raiz, bg="#9ED8F9")
        self.miFrame.config(bd=10,relief="groove")
        self.miFrame.pack(pady=(100, 0))

        labelMensaje = Label(self.miFrame, font=('Courier', 12), bg="#9ED8F9", text="Ingrese mensaje:")
        labelMensaje.grid(row=0, column=0, padx=5, pady=10)
        
        labelClave = Label(self.miFrame, font=('Courier', 12), bg="#9ED8F9", text="Ingrese Clave en caso de César:")
        labelClave.grid(row=1, column=0, padx=5, pady=10)
        
        inputMensaje = Entry(self.miFrame)
        inputMensaje.grid(row=0, column=1, padx=10)
        
        inputClave = Entry(self.miFrame)
        inputClave.grid(row=1, column=1, padx=10)

        frameBotones = Frame(self.raiz, bg="#9ED8F9")
        frameBotones.pack(pady=15)

        botonCifrarCesar = Button(frameBotones, text="Cifrar César", bg="#D5CF13")
        botonCifrarCesar.grid(row=0, column=0, padx=5)
        
        botonDescifrarCesar = Button(frameBotones, text="Descifrar César", bg="#D5CF13", command=lambda: self.descifrar(resultado_text))
        botonDescifrarCesar.grid(row=0, column=1, padx=5)
        
        resultado_text = Text(self.miFrame, font=('Courier', 12), bg="white", height=5, width=40, state=DISABLED)
        resultado_text.grid(row=2, column=0, padx=5, pady=10)

        botonCifrarAtbash = Button(frameBotones, text="Cifrar Atbash", bg="#D5CF13", command=lambda: self.cifrar(inputMensaje, resultado_text))
        botonCifrarAtbash.grid(row=0, column=2, padx=5)
        
        botonDescifrarAtbash = Button(frameBotones, text="Descifrar Atbash", bg="#D5CF13", command=lambda: self.descifrar(resultado_text))
        botonDescifrarAtbash.grid(row=0, column=3, padx=5)

    def mostrar_resultado(self, texto_cuadro, titulo, texto):
        """ Cuadro para mostrar el resultado de los mensajes.
            Matias Gonzalez
        """
        texto_cuadro.config(state=NORMAL)
        texto_cuadro.delete(1.0, END)
        texto_cuadro.insert(INSERT, titulo)
        texto_cuadro.insert(INSERT, "\n")
        texto_cuadro.insert(INSERT, texto)
        texto_cuadro.config(state=DISABLED)

    def iniciar(self):
        self.raiz.mainloop()

mi_interfaz = AtBashMensaje()
mi_interfaz.iniciar()