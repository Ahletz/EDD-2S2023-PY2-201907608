from tkinter import filedialog
from TablaH import *
from ArbolAVL import *
import csv

tablah = Tabla() #TABLA HASH
Arbol = Arbol_AVL() #ARBOL AVL


class Loger:

    def Ingresar(self, user, pasword):

        if user == "PM-201907608" and pasword == "PM-201907608":

           
            datos = tablah.table #OBTENCION DE LOS DATOS DE LA TABLA HASH

            for hash in datos.keys(): # FOR PARA OBTENER EL INDEX

                print("INDEX: "+hash) #IMPREISON DEL INDEX EN CONSOLA


            return "PM" #RETORNAR PM EN CASO DE QUE SEA EL PROJECT MANAGER
        
        elif user in tablah.table.values() and pasword in tablah.table.values() :

            datos = tablah.table #OBTENCION DE LOS DATOS DE LA TABLA HASH

            for hash in datos.keys(): # FOR PARA OBTENER EL INDEX

                print("INDEX: "+hash) #IMPREISON DEL INDEX EN CONSOLA


            return "USUARIO" #RETORNAR PM EN CASO DE QUE SEA UN USUARIO
        
        else:

            return "NO_IN" #EN CASO DE NO INGRESAR UN DATO VALIDO


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
            

        
            

