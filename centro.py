from usuarios import *
from canchas import Cancha
from usuarios import Cliente


class Centro:
    def __init__(self):
        
        self.__canchas=[]
        self.__clientes=[]

    def canchas(self):
        for x in self.__canchas:
            print(x)

    def clientes(self):
        for x in self.__clientes:
            print(x)
    
    def establecernuevoCosto(self,cancha,costo):
        cancha.establecernuevoCosto(costo)

    def canchasDeporte(self,deporte):
        cant=0
        print(" Canchas del deporte "+ deporte)
        for x in self.__canchas:
            if x.obtenerDeporte()==deporte:
                cant=cant+1
                print(x)     
        print(" Cantidad de canchas "+str(cant))

    def estaRegistrado(self,elemento):
        if isinstance(elemento,Cancha):
            if elemento in self.__canchas:
                return True
        if isinstance(elemento,Cliente):
            if elemento in self.__clientes:
                return True

    def registrarCliente(self,cliente):
        if isinstance(cliente,Cliente):
            if not self.estaRegistrado(cliente):
                self.__clientes.append(cliente)

    def registrarPago(self,cliente,monto):
        cliente.registrarMovimiento(monto)

    def registrarCancha(self,cancha):
        if isinstance(cancha,Cancha):
            if self.estaRegistrado(cancha):
                print("La cancha ya se encuentra registrada")
            else:
                self.__canchas.append(cancha)

    def registrarReserva(self,mes,dia,hora,cliente,cancha):
        if self.estaRegistrado(cliente) and cliente.estaHabilitado() and cliente.controlDeuda(): 
            if self.estaRegistrado(cancha) and cancha.estaHabilitada() and cancha.chequeoHorario(mes,dia,hora):
                if cancha.estaDisponible(mes,dia,hora):
                    cancha.nuevaReserva(mes,dia,hora,cliente,cancha)
                    return(" Registro de reserva Exitoso ")
        return(" Reserva Cancelada ")
        

    def desregistrarReserva(self,mes,dia,hora,cancha):
        for x in self.reservas(cancha):
            if x.desregistrarReserva(mes,dia,hora):
                print(" Reserva desregistrada correctamente")

    def desregistrarCancha(self,elemento):
        if isinstance(elemento,Cancha):
            if self.estaRegistrado(elemento):
                if not elemento.tieneReservas():
                    self.__canchas.remove(elemento)
                    print(" Se desregistro la cancha")
                else:
                    print(" No se pudo desregistrar la cancha ")

    def desregistrarCliente(self,elemento):
        if isinstance(elemento,Cliente):
            if self.estaRegistrado(elemento):
                if len(self.reservas(elemento))==0:
                    self.__clientes.remove(elemento)
                    print(" Se quito de la lista ")
                else:
                    print(" No se pudo quitar de la lista ")
            
   
    def reservas(self,elemento=None):   #devuelve una lista de reservas depende del parametro que se mande
        lista=[]

        if isinstance(elemento,Cancha):
            if self.estaRegistrado(elemento):
                for x in elemento.obtenerReservas():
                        lista.append(x)
             
        if isinstance(elemento,Cliente):
            if self.estaRegistrado(elemento):
                for x in self.__canchas:
                    for i in x.obtenerReservas(elemento):
                        lista.append(i)

        if elemento==None:
            for x in self.__canchas:
                for i in x.obtenerReservas():
                    lista.append(i)

        return lista

    def mostrarReservasActuales(self,elemento=None):
        for x in self.reservas(elemento):
            if x.esProxima():
                print(x)

    def mostrarReservasTotales(self,elemento=None):
        for x in self.reservas(elemento):
            print(x)

    def mostrarMorosos(self,cancha=None):
        cant=0

        if cancha==None:
            for x in self.__clientes:
                if x.obtenerSaldo()<0:
                    cant=cant+1
                    print(x)

        if cancha!=None:
            for x in cancha.obtenerReservas():
                cliente=x.obtenerCliente()
                if cliente.obtenerSaldo()<0:
                    cant=cant+1
                    print(cliente.nombre)
                    
        print("Cantidad de morosos:" + str(cant))

    def habilitarCliente(self,cliente):
        if self.estaRegistrado(cliente):
            cliente.habilitar()

    def deshabilitarCliente(self,cliente):
        if self.estaRegistrado(cliente):
            cliente.deshabilitar


    def consultaDisponible(self,mes,dia,hora,elemento=None):
        if isinstance(elemento,Cancha):
            if self.estaRegistrado(elemento):
                if elemento.estaDisponible(mes,dia,hora):
                    print(" Horario y cancha disponible para su reserva")
        else:
            for x in self.__canchas:
                if x.obtenerDeporte()==elemento:
                    if x.estaDisponible(mes,dia,hora):
                        print(x + "esta disponible")

    def saldo(self,cliente):
        if self.estaRegistrado(cliente):
            print(cliente.obtenerSaldo())

    def registrarEmpleado(self,empleado,cancha):
        for x in self.__canchas:
            if x.estaHabilitada():
                if empleado in x.obtenerEmpleados():
                    return(" El empleado ya se encuentra registrado ")
        cancha.registrarEmpleado(empleado)


    def tareasEmpleado(self,empleado):
        for x in self.__canchas:
            if empleado in x.obtenerEmpleados():
                print(" Tareas en la cancha: ")
                print(x)
                print(empleado.obtenerTareas())
        
    def asignarTarea(self,empleado,cancha,tarea):
        if self.estaRegistrado(cancha):
            if empleado in cancha.obtenerEmpleados():
                empleado.nuevaTarea(tarea)
    
    def quitarTarea(self,empleado,cancha,tarea):
        if self.estaRegistrado(cancha):
            if empleado in cancha.obtenerEmpleados():
                if tarea in empleado.obtenerTareas():
                    empleado.quitarTarea(tarea)

    def empleados(self,cancha=None):
        if cancha==None:
            for x in self.__canchas:
                for i in x.obtenerEmpleados():
                    print(i)
        if cancha!=None:
            if self.estaRegistrado(cancha):
                for i in cancha.obtenerEmpleados():
                    print(i)


    def empleadosDesocupados(self,cancha=None):
        print(" EMPLEADOS DESOCUPADOS ")
        if cancha==None:
            for x in self.__canchas:
                for i in x.obtenerEmpleados():
                    if i.estaOcupado()==False:
                        print(i)
        else:
            if self.estaRegistrado(cancha):
                for x in cancha.obtenerEmpleados():
                    if x.estaOcupado()==False:
                        print(x)

    def desregistrarEmpleado(self,empleado,cancha):
        if self.estaRegistrado(cancha):
            if empleado in cancha.obtenerEmpleados():
                cancha.remove(empleado)
    



                

        











                    






               


