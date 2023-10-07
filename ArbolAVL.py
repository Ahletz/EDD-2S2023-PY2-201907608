from NodoAVL import Nodo_AVL
import os

class Arbol_AVL():
    def __init__(self):
        self.raiz = None

    def Insertar(self, id, nombre, prioridad):
        self.raiz = self.InsertarNodo(id, nombre, prioridad, self.raiz)

    def Altura(self, raiz):
        condicion = raiz == None
        return 0 if condicion else raiz.altura
    
    def Equilibrio(self, raiz):
        condicion = raiz == None
        return 0 if condicion else (self.Altura(raiz.derecho) - self.Altura(raiz.izquierdo))
    
    def RotacionI(self, raiz):
        raiz_derecho = raiz.derecho
        hijo_izquierdo = raiz_derecho.izquierdo
        raiz_derecho.izquierdo = raiz
        raiz.derecho = hijo_izquierdo
        raiz.altura = 1 + max(self.Altura(raiz.izquierdo),self.Altura(raiz.derecho))
        raiz.factor_equilibrio = self.Equilibrio(raiz)
        raiz_derecho.altura = 1 + max(self.Altura(raiz_derecho.izquierdo),self.Altura(raiz_derecho.derecho))
        raiz_derecho.factor_equilibrio = self.Equilibrio(raiz_derecho)
        return raiz_derecho
    
    def RotacionD(self, raiz):
        raiz_izquierdo = raiz.izquierdo
        hijo_derecho = raiz_izquierdo.derecho
        raiz_izquierdo.derecho = raiz
        raiz.izquierdo = hijo_derecho
        raiz.altura = 1 + max(self.Altura(raiz.izquierdo), self.Altura(raiz.derecho))
        raiz.factor_equilibrio = self.Equilibrio(raiz)
        raiz_izquierdo.altura = 1 + max(self.Altura(raiz_izquierdo.izquierdo), self.Altura(raiz_izquierdo.derecho))
        raiz_izquierdo.factor_equilibrio = self.Equilibrio(raiz_izquierdo)
        return raiz_izquierdo
    
    def InsertarNodo(self, id, nombre, prioridad, raiz):
        if raiz is None:
            return Nodo_AVL(id, nombre, prioridad)
        else:
            if raiz.id == id:
                raiz.id = id
            elif raiz.id > id:
                raiz.izquierdo = self.InsertarNodo(id, nombre, prioridad, raiz.izquierdo)
            elif raiz.id < id:
                raiz.derecho = self.InsertarNodo(id, nombre, prioridad, raiz.derecho)
        #Luego de insercion, procedemos a realizar rotaciones
        raiz.altura = 1 + max(self.Altura(raiz.izquierdo),self.Altura(raiz.derecho))
        balanceo = self.Equilibrio(raiz)
        raiz.factor_equilibrio = balanceo

        if balanceo > 1 and id > raiz.derecho.id:#Rotacion Simple a la Izquierda
            return self.RotacionI(raiz)
        if balanceo < -1 and id < raiz.izquierdo.id:#Rotacion Simple a la Derecha
            return self.RotacionD(raiz)
        if balanceo > 1 and id < raiz.derecho.id:#Rotacion Doble a la Izquierda
            raiz.derecho = self.RotacionD(raiz.derecho)
            return self.RotacionI(raiz)
        if balanceo < -1 and id > raiz.izquierdo.id:#Rotacion Doble a la Derecha
            raiz.izquierdo = self.RotacionI(raiz.izquierdo)
            return self.RotacionD(raiz)
        return raiz
    

    def graficar(self):
        cadena = ''
        archivo = "AVL.jpg"
        a = open("AVL.dot","w")
        if self.raiz is not None:
            cadena += "digraph arbol {"
            cadena += self.retornarValoresArbol(self.raiz, 0)
            cadena += "}"
        a.write(cadena)
        a.close()
        os.system("dot -Tjpg AVL.dot -o " + archivo)
    

    def retornarValoresArbol(self, raiz, id):
        cadena = ''
        numero = id + 1
        if raiz is not None:
            cadena += "\""
            cadena += "PY-"+str(raiz.id)+ "\n" + raiz.nombre + "\n" + raiz.prioridad  
            cadena += "\" ;\n"
            if(raiz.izquierdo is not None and raiz.derecho is not None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"{}\" -> {} \"{}\" -> {}".format(raiz.id, self.retornarValoresArbol(raiz.izquierdo, numero), raiz.id, self.retornarValoresArbol(raiz.derecho, numero))
                cadena += "{" + "rank=same" + "\"{}\" -> \"{}\" [style=invis]; ".format(raiz.izquierdo.id, raiz.derecho.id) + "} \n"
            elif(raiz.izquierdo is not None and raiz.derecho is None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"{}\" -> {} \"{}\" -> x{}[style=invis];\n".format(raiz.id, self.retornarValoresArbol(raiz.izquierdo, numero), raiz.id, numero)
                cadena += "{" + "rank=same " + "\"{}\" -> x{} [style=invis]; ".format(raiz.izquierdo.id, numero) + "} \n"
            elif(raiz.izquierdo is None and raiz.derecho is not None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"{}\" -> x{}[style=invis]; \n \"{}\" -> {}".format(raiz.id, numero, raiz.id, self.retornarValoresArbol(raiz.derecho, numero))
                cadena += "{" + "rank=same " + "x{} -> \"{}\" [style=invis]; ".format(numero, raiz.derecho.id) + "} \n"
        return cadena