from tkinter import *
from tkinter import ttk

from Acciones_login import *
from Ventana import *

abrir = PM()

pulsado = Loger()

class Logear:

    

    def __init__(self) :
        self.root = Tk() #IMPLEMNTACION DE UNA VENTANA
        self.root.title("LOGIN") #NOMBRE DE LA VENTANA
        self.root.geometry("350x500+600+150") #DIMENSIONES DE LA VENTANA: ANCHO + ALTO + POSICION EN X + POSICION EN Y
        self.root.config(bg="cyan3") #COLOR DE LA VENTANA
        self.root.resizable(0,0) #NO HACER MAS GRANDE LA VENTANA

        self.Entrar() #BOTONES
        self.Cajas() #CAJAS DE TEXTO
        self.Text() #labels 


        self.root.mainloop() #MANTENER LA VENTANA ABIERTA

    def Entrar(self):

        Boton = Button(text="INGRESAR", command=self.Ingresar).place(x=150, y=350)

    def Cajas(self):

        self.caja1 =Entry()
        self.caja1.place(x=50,y=150,height=30,width=250)
        self.caja2 =Entry()
        self.caja2.place(x=50,y=250,height=30,width=250)

    def Text(self):

        texto1 = Label(text="USUARIO",bg="cyan2").place(x=50,y=100,height=30,width=250)
        texto2 = Label(text="CONTRASEÑA",bg="cyan2").place(x=50,y=200,height=30,width=250)

    def Ingresar(self):

        usuario = self.caja1.get() #OBTENER EL CONTENIDO DE LAS TEXTBOX
        pasword = self.caja2.get()

        entro = pulsado.Ingresar(usuario, pasword)

        if entro == True:

            self.root.destroy()
            abrir.Manager()
            self.__init__()

        #print("usuario: ",usuario," contraseña: ",pasword)
        
        









        