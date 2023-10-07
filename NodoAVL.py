class Nodo_AVL():
    
    def __init__(self, id, nombre, prioridad):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad
        self.izquierdo = None
        self.derecho = None
        self.altura = 1
        self.factor_equilibrio = 0
