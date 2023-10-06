from TablaH import *

tablah = Tabla() #TABLA HASH

class Loger:

    def Ingresar(self, user, pasword):

        if user == "PM-201907608" and pasword == "PM-201907608":

            tablah.Insertar("FEDEV-001","LEONARDO MARTINEZ","LEO123","FRONTEND DEVELOPER")
            print("1")
            tablah.Insertar("FEDEV-001","LEONARDO MAR","LEO124","FRONTEND DEVELOPER")
            print("2")

            tablah.Search("FEDEV-001","LEO124")
            print("1")
            tablah.Search("FEDEV-001","LEO123")
            print("2")
            return True 
        

        
            

