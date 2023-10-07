#IMPORTAR LIBRERIAS TKINTER
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import csv

#IMPORTAR COMPONENTES

from Acciones_login import *

acciones = Loger()

class Inicio:

    def __init__(self) :
        self.rootLOG = Tk() #IMPLEMNTACION DE UNA VENTANA
        self.rootLOG.title("LOGIN") #NOMBRE DE LA VENTANA
        self.rootLOG.geometry("350x500+600+150") #DIMENSIONES DE LA VENTANA: ANCHO + ALTO + POSICION EN X + POSICION EN Y
        self.rootLOG.config(bg="cyan3") #COLOR DE LA VENTANA
        self.rootLOG.resizable(0,0) #NO HACER MAS GRANDE LA VENTANA

        self.Entrar() #BOTONES
        self.Cajas() #CAJAS DE TEXTO
        self.Text() #labels 

        self.rootLOG.mainloop() #MANTENER LA VENTANA ABIERTA

    def Entrar(self):

        Boton = Button(text="INGRESAR", command= self.Ingresar).place(x=150, y=350)

    def Cajas(self):

        self.caja1 =Entry()
        self.caja1.place(x=50,y=150,height=30,width=250)
        self.caja2 =Entry(show="*")
        self.caja2.place(x=50,y=250,height=30,width=250)

    def Text(self):

        texto1 = Label(text="USUARIO",bg="cyan2").place(x=50,y=100,height=30,width=250)
        texto2 = Label(text="CONTRASEÑA",bg="cyan2").place(x=50,y=200,height=30,width=250)

    def Obtener(self):

        return self.caja1.get(), self.caja2.get()
    
    def Ingresar(self):

        usuario, password = self.Obtener()

        entro = acciones.Ingresar(usuario,password)

        if entro == "PM":

            self.rootLOG.destroy()
            self.Principal(1)
            self.__init__()
           
                        
        elif entro == "USUARIO":

            self.rootLOG.destroy()
            self.Principal(2)
            self.__init__()

        elif entro == "NO_IN":
            messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

    
    def Principal(self, indice) :

        self.root = Tk() #IMPLEMNTACION DE UNA VENTANA
        self.root.title("PROJECT MANAGER") #NOMBRE DE LA VENTANA
        self.root.geometry("850x600+100+150") #DIMENSIONES DE LA VENTANA: ANCHO + ALTO + POSICION EN X + POSICION EN Y
        self.root.config(bg="cyan4") #COLOR DE LA VENTANA
        self.root.resizable(0,0) #NO HACER MAS GRANDE LA VENTANA
        
        if indice == 1:
            self.ComponenetesMG()
        elif indice == 2:
            pass

        self.root.mainloop() #MANTENER LA VENTANA ABIERTA


    def ComponenetesMG(self):

        boton1 = Button(text="CARGAR CSV", command= self.CargarTabla)
        boton2 = Button(text="CARGAR JSON", command=self.Abrir_Json_AVL)
        boton3 = Button(text="PROYECTOS Y TAREAS", command=self.Area_texto_Json)
        boton4 = Button(text="EMPLEADOS", command=self.tabla_empleados)
        boton5 = Button(text="REPORTE PROYECTOS",command=self.Mostrar_Arbol_AVL)
        boton6 = Button(text="REPORTE TAREAS")

        imagen = PhotoImage(file="usuario.png") #IMAGEN USUARIO

        Texto = Label(text="PM-201907608")
        Img = Label(image=imagen)

        boton1.place(x=50,y=50)
        boton2.place(x=50,y=75)
        boton3.place(x=130,y=120)
        boton4.place(x=50,y=120)
        boton5.place(x=300,y=120)
        boton6.place(x=450,y=120)

        Texto.place(x=400,y=50)
        Texto.config(bg="cyan3",font=("Arial",16))

        Img.place(x=600,y=50)
        Img.config(width=100,height=100)

        self.tabla_empleados()

        
    def tabla_empleados(self):

        # Crear un Treeview con 4 columnas
        self.tree = ttk.Treeview( columns=("Índice", "ID", "Nombre", "Puesto"))

        # Configurar las columnas
        self.tree.heading("#1", text="Índice")
        self.tree.heading("#2", text="ID")
        self.tree.heading("#3", text="Nombre")
        self.tree.heading("#4", text="Puesto")

        self.tree.pack(padx=20,pady=170)

    def Area_texto_Json(self):

        self.area_texto = Text(height=750, width=300, state='disabled')
        self.area_texto.place(x=50,y=150)
        self.Insertar_texto()

    def Insertar_texto(self):
        self.area_texto.config(state="normal")
        self.area_texto.insert("contenido_Json")
        self.area_texto.config(state="disabled")


    def ComponenetesUSER(self):

        boton1 = Button(text="CARGARCSV")
        boton2 = Button(text="CARGAR JSON")
        boton3 = Button(text="PROYECTOS Y TAREAS")
        boton4 = Button(text="EMPLEADOS")
        boton5 = Button(text="REPORTE PROYECTOS")
        boton6 = Button(text="REPORTE TAREAS")

        imagen = PhotoImage(file="usuario.png") #IMAGEN USUARIO

        Texto = Label(text="PM-201907608")
        Img = Label(image=imagen)

        boton1.place(x=50,y=50)
        boton2.place(x=50,y=75)
        boton3.place(x=130,y=120)
        boton4.place(x=50,y=120)
        boton5.place(x=300,y=120)
        boton6.place(x=450,y=120)

        Texto.place(x=400,y=50)
        Texto.config(bg="cyan3",font=("Arial",16))

        Img.place(x=600,y=50)
        Img.config(width=100,height=100)

    def CargarTabla(self):

        direccion = acciones.CargarCSV()
        if direccion:
            try:
                # Intenta abrir y leer el archivo CSV
                with open(direccion, newline='') as csvfile:
                    lector_csv = csv.reader(csvfile)
                    next(lector_csv)  # Omitir la primera línea (títulos de las columnas)
                    for fila in lector_csv:
                        # Suponiendo que cada fila tiene cuatro campos (id, nombre, contraseña y puesto)
                        id, nombre, contraseña, puesto = fila

                        index = tablah.CalculoInd(id)

                        No = str(tablah.NewIndex(index))
                        
                        self.tree.insert("", "end", values=(No,id,nombre, puesto,"")) #ingresar los datos dentro de la tabla hash

            except Exception as e:
               print("Error al abrir el archivo CSV:", e)

    def Abrir_Json_AVL(self):

        acciones.cargar_archivo_json()


    def Mostrar_Arbol_AVL(self):

        Arbol.graficar()


    







