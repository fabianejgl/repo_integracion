    #------6------
class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @edad.setter
    def edad(self,nueva_edad):
        if nueva_edad < 0:
            print("La edad no puede ser menor a 0")
        else:
            self.__edad = nueva_edad

    @dni.setter
    def dni(self,nuevo_dni):
        if len(nuevo_dni) == 8:
            self.__dni = nuevo_dni
        else:
            print("El DNI debe tener 9 dígitos")
    
    def mostrar(self):
        print("DATOS DE LA PERSONA:")
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")
    
    def Es_mayor_de_edad(self):
        return self.__edad >= 18


persona1 = Persona()
persona1.nombre='fabian'
persona1.edad=18
persona1.dni="94484630"
persona1.mostrar()
persona1.Es_mayor_de_edad()