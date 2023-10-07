from NH import *

class Tabla():
    def __init__(self) -> None:
        self.table = {} #TUPLA PARA REALIZAR EL HASH
        self.tamaño = 5
        self.utility = 0

    def Insertar(self, id, nombre, password, puesto): #FUNCION DE INSERTAR NUEVO 

        index = self.CalculoInd(id) #CALCULAR INDICE DE LA TABLA HASH
        new = NH(id,nombre,password,puesto) #CREACION DE NODO TABLA HASH

        if index <self.tamaño: #TAMAÑO DE LA TABLA COMPROBACION
            try:
                if not (index in self.table): #SI EL INDICE AUN NO ESTA DENTRO DE LA TABLA
                    self.table[index] = new #SE AGREGA EL VALOR DE LA TABLA HASH Y EL CONTENIDO A LA TUPLA
                    self.utility +=1 # SE AGREGA 1 DATO A LA UTILIZACION DE LA TABLA
                    self.capacidad() #COMPROBACION DE LA TABLA HASH Y SU TAMAÑO PARA REDIMENSIONAR SI ES NECESARIO
                else:

                    contador = 1 #CONTADOR INTENTOS
                    index = self.ReIndex(id,contador) #NUEVO INDICE MEDIANTE FUNCION
                    while (index in self.table): #BUSCAR NUEVO REINDEX DENTRO DE TABLA EN CASO DE EXISTIR
                        contador += 1 #AUMENTO DE INTENTOS 
                        index = self.ReIndex(id, contador) #NEUVA INDEX
                    self.table[index] = new #AGREGAR INDEX A TABLA Y DATOS DE TUPLA
                    self.utility += 1 #AUMENTO UTILIZACION
                    self.capacidad() #CAPACIDAD TABLA HASH
                    
            
            except:
               print("FATAL ERROR INSERT!")


    def CalculoInd(self, id): #CALCULO DEL INDICE DEL NUEVO DATO EN LA TABLA HASH

        total = 0 #VARIABLE SUMA

        for caracter in id: #CALCULO DE EL VALOR MEDIANTE FOR Y VALOR ASCII
            valorAscii = ord(caracter)
            total += valorAscii
        
        index = total % self.tamaño #CALCULO DEL INDICE

        return index #RETORNO DEL INDICE
    

    def capacidad(self): #CAPACIDAD DE LA TABLA HASH

        actual = self.tamaño*0.70 #CALCULO DEL CONSUMO DEL 70% DE LA TABLA

        if self.utility > actual: #COMPROBACION DEL TAMAÑO DE LA TABLA
            self.tamaño  = self.NuevoTamaño() #FIJACION DEL NUEVO TAMAÑO DE LA TALBA
            self.utility = 0 #REINICIO UTILIZACIONES
            self.RIn() #REORDENAMIENTO DE LOS DATOS YA ALMACENADOS

    def NuevoTamaño(self): #IMPLEMENTACION DE LA SERIE DE FIBONACCI PARA EL NUEVO TAMAÑO DE LA TABLA

        contador = 0
        a, b = 0, 1 #0, 1, 1, 2, 3, 5, 8, 13, 21, 34....
        while contador < 15:
            contador += 1
            if a > self.tamaño:
                return a
            a, b = b, a + b
        return a
    
    def RIn(self): #REINSERTAR UN DATO EN TABLA 

        Taux = self.table #TABLA AUXILIAR PARA LA INSERCION
        self.table = {}
        
        for _, valor in Taux.items():
            self.Insertar(valor.id, valor.nombre, valor.password, valor.puesto)

    


    def ReIndex(self, id, intento): #NUEVO INDICE A UN INDICE YA EXISTENTE
        newIndex = self.CalculoInd(id) + (intento*intento) #NUEVO INDICE = INDICE CALCULADO + INTENTO AL CUADRADO
        return self.NewIndex(newIndex) #DEVUELVE EL NUEVO INDICE
    
    def NewIndex(self, newId): #NUEVO INDICE

        newPosicion = 0 
        if newId < self.tamaño: # COMRPOBACION EXISTA DENTRO DEL TAMAÑO DE LA TABLA

            newPosicion = newId #COLOCACION

        else: 

            newPosicion = newId - self.tamaño #CAMBIO DE LUGAR SI EXCEDE EL TAMAÑO DE LA TABLA
            newPosicion = self.NewIndex(newPosicion) #AGREGAR A LA TABLA HASH EN POSICION

        return newPosicion #RETORNAR POSICION
    

    def Search(self, id, password): #BUSCAR UN EMPLEADO EN LA TABLA HASH

        index = self.CalculoInd(id) #NUMERO DEL ID BUSCADO EN LA TABLA

        if index < self.tamaño: #COMRPOBACION TAMAÑO TABLA

            try:
                if (index in self.table): #SI LO ENCUENTRA EN TABLA
                    
                    empleado = self.table[index]
                    if empleado.id == id and empleado.password == password: #COMPARAR DATOS INGRESADOS
                        print("si")
                        return True #DEVOLVER VERDADERO
                elif not (index in self.table): #DE NO ENCONTRAR EL USUARIO
                    print("no")
                    return False
                else: #EN CASO DE QUE EL INDICE ESTE COLISIONADO SE UTILIZA RE INDEX PARA BUSCAR EL INDICE
                    contador = 1
                    index = self.ReIndex(id, contador)
                    while not(index in self.table):
                        contador += 1
                        index = self.ReIndex(id, contador)
                        empleado = self.table[index]
                        if empleado.id == id and empleado.password == password:
                            print("si")
                            return True
            except:
                 print("FATAL ERROR SERCH!")

        
        return False






    

