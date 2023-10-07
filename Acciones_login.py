from tkinter import filedialog
from TablaH import *
from ArbolAVL import *
import csv, json

tablah = Tabla() #TABLA HASH
Arbol = Arbol_AVL() #ARBOL AVL

global contenido_Json

class Loger:

    def Ingresar(self, user, pasword):

        if user == "PM-201907608" and pasword == "PM-201907608":

           
            datos = tablah.table #OBTENCION DE LOS DATOS DE LA TABLA HASH

            for hash in datos.keys(): # FOR PARA OBTENER EL INDEX

                print("INDEX: "+str(hash)) #IMPREISON DEL INDEX EN CONSOLA


            return "PM" #RETORNAR PM EN CASO DE QUE SEA EL PROJECT MANAGER
        
        elif user in tablah.table.values() and pasword in tablah.table.values() :

            datos = tablah.table #OBTENCION DE LOS DATOS DE LA TABLA HASH

            for hash in datos.keys(): # FOR PARA OBTENER EL INDEX

                print("INDEX: "+str(hash)) #IMPREISON DEL INDEX EN CONSOLA


            return "USUARIO" #RETORNAR PM EN CASO DE QUE SEA UN USUARIO
        
        else:

            return "NO_IN" #EN CASO DE NO INGRESAR UN DATO VALIDO
        
    def CargarCSV(self):

        direccion = self.Cargar_csv()

        return direccion


    def Cargar_csv(self):

        archivo_csv = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

        if archivo_csv:
            try:
                # Intenta abrir y leer el archivo CSV
                with open(archivo_csv, newline='') as csvfile:
                    lector_csv = csv.reader(csvfile)
                    next(lector_csv)  # Omitir la primera línea (títulos de las columnas)
                    for fila in lector_csv:
                        # Suponiendo que cada fila tiene cuatro campos (id, nombre, contraseña y puesto)
                        id, nombre, contraseña, puesto = fila
                        
                        tablah.Insertar(id,nombre,contraseña, puesto) #ingresar los datos dentro de la tabla hash

            except Exception as e:
                print("Error al abrir el archivo CSV:", e)

        return archivo_csv
    

    def cargar_archivo_json(self):
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if ruta_archivo:
            datos = self.leer_datos_desde_archivo(ruta_archivo)
            if datos:
                proyectos = datos.get("Proyectos", [])  # Variable título principal
                for proyecto in proyectos:
                    id_proyecto = proyecto.get("id", "")  # ID PROYECTO
                    nombre_proyecto = proyecto.get("nombre", "")  # NOMBRE PROYECTO
                    prioridad = proyecto.get("prioridad", "")  # PRIORIDAD
                    tareas = proyecto.get("tareas", [])  # ARREGLO DE TAREAS

                    print(f"Proyecto: {nombre_proyecto} (ID: {id_proyecto}, Prioridad: {prioridad})")  # Datos capturados para árbol AVL

                    #contenido_Json += id_proyecto+" "+nombre_proyecto + " " +prioridad +"\n" 

                    # datos árbol AVL
                    Arbol.Insertar(id_proyecto, nombre_proyecto, prioridad)

                    # TAREAS ARBOL B
                    for tarea in tareas:
                        nombre_tarea = tarea.get("nombre", "")  # NOMBRE DE LA TAREA
                        empleado = tarea.get("empleado", "")  # EMPLEADO
                        print(f"  Tarea: {nombre_tarea}, Empleado: {empleado}")  # Datos capturados para árbol B

                        #contenido_Json += "\t -"+nombre_tarea + " " + empleado+"\n" 
            else:
                print("No se pudieron cargar los datos desde el archivo.")
        else:
            print("No se seleccionó ningún archivo.")

    def leer_datos_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos = json.load(archivo)
                return datos
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no se encontró.")
            return None
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON '{nombre_archivo}'.")
            return None

    

    


    
            

        
            

