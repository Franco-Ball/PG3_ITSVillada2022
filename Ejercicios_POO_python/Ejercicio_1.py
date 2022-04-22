#---------------------- CLASE PERSONA ----------------------#
class Persona:

    def inicializar(self,name):
        self.nombre = name 
    
    def imprimir(self): 
        print(f"Nombre : {self.nombre}")

#---------------------- CODIGO ----------------------#

persona1 = Persona()
persona1.inicializar(input("Ingrese el nombre de la persona: "))
persona1.imprimir()

persona2 = Persona()
persona2.inicializar(input("Ingrese el nombre de la persona: "))
persona2.imprimir()

