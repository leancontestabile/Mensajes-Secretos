#Funciones para integrar el Objetivo 1 con la interfaz gráfica del Objetivo 3.

from Objetivo_1 import cifrado_cesar

def boton_cifrado_cesar(inputMensaje, inputClave, cifrado):
    """
    La función recibe 3 parámetros que son variables contenidas en la interfaz gráfica, a las dos primeras se les aplica el método get() 
    para conseguir la información de los cuadros de texto (Entry), y luego se invoca a la función del objetivo 1 para cifrar el mensaje ingresado 
    con su clave correspondiente, que se muestra en la interfaz utilizando la última variable ingresada como parámetro (otro Label).
    
    Mutazzi Nicolás Rocco
    """
    mensaje = inputMensaje.get()
    clave = int(inputClave.get())
    mensaje_cifrado = cifrado_cesar(mensaje, clave)
    cifrado.config(text=mensaje_cifrado)

def boton_descifrado_cesar(inputMensaje, inputClave, descifrado):
    """
    Lo mismo que la función del botón de cifrado, solamente que ahora se utiliza la clave negativa, para descifrar en vez de cifrar.
    
    Mutazzi Nicolás Rocco
    """
    mensaje = inputMensaje.get()
    clave = int(inputClave.get())
    mensaje_descifrado = cifrado_cesar(mensaje, -clave)
    descifrado.config(text=mensaje_descifrado)
    