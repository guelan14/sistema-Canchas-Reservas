from datetime import date
from reserva import Reserva

class Cancha():
    numCancha=0
      
    def __init__(self,deporte,direccion,costo):
        Cancha.numCancha=Cancha.numCancha+1

        self.numCancha=Cancha.numCancha
        self.deporte=deporte
        self.direccion=direccion
        self.costo=costo
        self.habilitada=True
        self.reservas=[]
        self.empleados=[]

    def __str__(self):
        return "NUM:"+str(self.numCancha)+" Deporte " +self.deporte +" Direccion: "+self.direccion

    def nuevoCosto(self,costo):
        self.costo=costo

    def nuevoDeporte(self,deporte):
        self.deporte=deporte
        
    def habilitar(self):
        self.habilitada=True

    def deshabilitar(self):
        self.habilitada=False

    def estaHabilitada(self):
        return self.habilitada

    def obtenerDeporte(self):
        return self.deporte

    def tieneReservas(self):
        if len(self.reservas) > 0:
            for x in self.reservas:
                if x.esProxima():   
                    return True
        return False

    def obtenerReservas(self,cliente=None):
        lista=[]
        if cliente==None:
            for x in self.reservas:
                    lista.append(x)           
            return lista

        if cliente!=None:
            for x in self.reservas:
                if x.obtenerCliente()==cliente:
                    lista.append(x)
            return lista


    def estaDisponible(self,mes,dia,hora):
        for x in self.reservas:
            if x.compararHorario(mes,dia,hora):
                return False
        return True
        

    def chequeoHorario(self,mes,dia,hora):
        if mes>0 and mes<13:
            if (hora>=19 and hora<=23) or (hora>=8 and hora<=12):
                return True
        return False


    def nuevaReserva(self,mes,dia,hora,cliente,cancha):
        cliente.registrarMovimiento(self.costo*(-1))
        reserva=Reserva(mes,dia,hora,cliente,cancha)
        self.reservas.append(reserva)

    def desregistrarReserva(self,mes,dia,hora):
        for x in self.obtenerReservas():
            if x.mismoHorario(mes,dia,hora):
                self.reservas.remove(x)
                x.cliente.desregistrarMovimiento(self.costo)

    def registrarEmpleado(self,empleado):
        if empleado not in self.empleados:
            self.empleados.append(empleado)

    def obtenerEmpleados(self):
        return self.empleados

        



    
        
