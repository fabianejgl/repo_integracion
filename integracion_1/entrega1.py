#Mantuve del ej 6 que Persona podía inicializarse con datos vacíos, sino borarr los =
class Persona:
    def __init__(self, nombre="NN", edad=0):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value

    def __str__(self) -> str:
        return f"La persona es {self.__nombre} de {self.__edad} de edad"
    
    def mostrar(self):
        print(f"La persona es {self.__nombre}")
        print(f"Edad: {self.edad}")



class Cuenta:
    def __init__(self, titular:Persona, cantidad = 0) -> None: #:Persona agregado
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter                               #NO es necesario si uso setter de Persona? Preguntar
    def titular(self, titular_nuevo):
         self._titular = titular_nuevo
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"El titular de la cuenta es {self.__titular.mostrar()}")
        print(f"Edad: {self.__titular.edad}")
        print(f"Saldo en cuenta: {self.__cantidad}")
    
    def ingresar(self, dinero):
        if dinero > 0:
            self.__cantidad += dinero
    
    def retirar(self, dinero):
        self.__cantidad -= dinero

# persona1 = Persona("Fabian", 22)
# cuenta1 = Cuenta(persona1)
# cuenta1.mostrar()
    # #cuenta1.titular = "Fabian"            este no va porque uso el setter.nombre de Persona.
# cuenta1.titular.nombre = "Fabian"
# cuenta1.ingresar(10)
# cuenta1.mostrar()
# cuenta1.retirar(20)
# cuenta1.mostrar()


    #------7------
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad:float=0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nueva_bonif):
        if nueva_bonif < 0:
            raise ValueError("La bonificación debe ser positiva")
        self.__bonificacion = nueva_bonif

    def es_titular_valido(self):
        return self.titular.edad >= 25

    def retirar(self, dinero):
        if self.es_titular_valido():
            super().retirar(dinero)
            print("El retiro fue exitoso")
        else:
            print("No puede retirar pues no es titular válido")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"La bonificación es de {self.__bonificacion}%")




#---Main---

print("")
persona2 = Persona()
cuenta2 = CuentaJoven(persona2,bonificacion = 50)
cuenta2.mostrar()
print("")

#cuenta1.titular = "Fabian"            este no va porque uso el setter.nombre de Persona.
cuenta2.titular.nombre = "Fabian"
cuenta2.titular.edad = 25
cuenta2.ingresar(10)
cuenta2.mostrar()
print("")
print(cuenta2.titular)

cuenta2.retirar(20)
print("")

cuenta2.mostrar()