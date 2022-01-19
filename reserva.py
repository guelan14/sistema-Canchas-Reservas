from datetime import date


class Reserva():
    numReserva=0
    

    def __init__(self,mes,dia,hora,cliente,cancha):
        Reserva.numReserva+=1                       

        self.numReserva=Reserva.numReserva
        self.mes=mes
        self.dia=dia
        self.hora=hora
        self.cliente=cliente
        self.cancha=cancha


    def __str__(self):
        return("Reserva N: "+str(self.numReserva)+" Mes: "+str(self.mes)+" Dia: "+str(self.dia)+" HORA: "+str(self.hora)+" CLIENTE: "+self.cliente.nombre+" Cancha N" + str(self.cancha.numCancha)+" "+ self.cancha.deporte)

    def obtenerCliente(self):
        return self.cliente

    def compararHorario(self,mes,dia,hora):
        if self.mes==mes and self.dia==dia and self.hora==hora:
            return True
        else:
            return False

    def esProxima(self):
        if self.mes==date.today().month and self.dia>=date.today().day: 
            return True
        elif self.mes>date.today().month:
            return True
        else:
            return False













