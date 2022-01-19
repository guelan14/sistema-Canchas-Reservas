from canchas import *
import datetime


class Persona:
    def __init__(self,nombre,apellido,telefono):

        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono

    def __str__(self):
        return("Persona: "+self.nombre+" "+self.apellido)

class Empleado(Persona):
    def __init__(self,nombre_empleado,apellido_empleado,telefono_empleado):
        super().__init__(nombre_empleado,apellido_empleado,telefono_empleado)
        self.desocupado=True
        self.tareas=[]

    def nuevaTarea(self,tarea):
        self.tareas.append(tarea)
        self.desocupado=False

    def quitarTarea(self,tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
        else:
            "no tiene esta tarea"
        if len(self.tareas)==0:
            self.desocupado=True

    def obtenerTareas(self):
        return self.tareas

    def estaOcupado(self):
        if self.desocupado==False:
            return True
        else:
            return False

    def __str__(self):
        return(" Empleado: "+ self.nombre+ " "+self.apellido)



class Cliente(Persona):
    idCliente=0

    def __init__(self,nombre_cliente,apellido_cliente,telefono_cliente):
        super().__init__(nombre_cliente,apellido_cliente,telefono_cliente)
        Cliente.idCliente+=1
        
        self.__id=Cliente.idCliente
        self.habilitado=True
        self.movimientos=[]


    @property
    def id(self):
        return self.__id

    def estaHabilitado(self):
        if self.habilitado:
            return True
    
    def habilitar(self):
        self.habilitado=True
    
    def deshabilitar(self):
        self.habilitado=False

    def registrarMovimiento(self,monto):
        self.movimientos.append(monto)

    def desregistrarMovimiento(self,monto):
        self.movimientos.remove(monto)

    def obtenerSaldo(self):
        saldo=sum(self.movimientos)
        return saldo

    def controlDeuda(self):
        if self.obtenerSaldo()>(-2000):
            return True
        return False



    def __str__(self):
        return("Cliente N: "+str(self.__id)+" "+self.nombre+" "+str(self.apellido))







