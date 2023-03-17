#Mantuve del ej 6 que Persona podía inicializarse con datos vacíos, sino borarr los =
class Persona:
    def __init__(self, nombre="NN", edad=0):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value



class Cuenta:
    def __init__(self, titular, cantidad = 0) -> None:
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular
    
    # @titular.setter                               #NO es necesario si uso setter de Persona
    # def titular(self, nuevo_nombre):
    #     self._titular = nuevo_nombre
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print(f"El titular de la cuenta es {self._titular.nombre}")
        print(f"Edad: {self._titular.edad}")
        print(f"Saldo en cuenta: {self._cantidad}")
    
    def ingresar(self, dinero):
        if dinero > 0:
            self._cantidad += dinero
    
    def retirar(self, dinero):
        self._cantidad -= dinero

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
    def __init__(self, titular, cantidad=0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nueva_bonif):
        self._bonificacion = nueva_bonif

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
        print(f"La bonificación es de {self._bonificacion}%")




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

cuenta2.retirar(20)
print("")

cuenta2.mostrar()