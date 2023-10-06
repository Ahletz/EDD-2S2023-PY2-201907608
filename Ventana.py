from tkinter import *
from tkinter import ttk

class PM:

    def Manager(self) :

        self.root = Tk() #IMPLEMNTACION DE UNA VENTANA
        self.root.title("PROJECT MANAGER") #NOMBRE DE LA VENTANA
        self.root.geometry("500x500+100+150") #DIMENSIONES DE LA VENTANA: ANCHO + ALTO + POSICION EN X + POSICION EN Y
        self.root.config(bg="cyan4") #COLOR DE LA VENTANA
        self.root.resizable(0,0) #NO HACER MAS GRANDE LA VENTANA

        self.root.mainloop() #MANTENER LA VENTANA ABIERTA

        
        