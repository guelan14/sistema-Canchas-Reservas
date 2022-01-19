from centro import Centro
from canchas import *
from usuarios import *


centro=Centro()

c1=Cancha("Futbol","Liniers 228",400)
print(c1)

c2=Cancha("Basquet","Avenida 229",1000)
print(c2)

centro.registrarCancha(c1)
centro.registrarCancha(c2)

p1=Cliente("Pedro","Ramon",654654984)
p2=Cliente(" Jorge", " Rodriguez", 15455)

centro.registrarCliente(p1)
centro.registrarCliente(p2)

centro.registrarReserva(8,4,8,p1,c1)
centro.registrarReserva(5,4,8,p2,c1)
centro.registrarReserva(4,4,8,p2,c2) 

p3=Empleado("Fernando","Uefi",34885858)
p4=Empleado("Evelyn","catalina",485858585)

centro.canchasDeporte("Futbol")

centro.mostrarMorosos()
    
centro.desregistrarCliente(p1)
centro.clientes()

centro.registrarPago(p1,1400)
centro.saldo(p1)

centro.registrarEmpleado(p3,c1)
centro.registrarEmpleado(p4,c2)

centro.asignarTarea(p3,c1,"Limpiar")
centro.asignarTarea(p3,c1," Revisar condicion de butacas")

centro.empleados(c1)
centro.tareasEmpleado(p3)
centro.empleadosDesocupados()

centro.mostrarReservasActuales(c1)   #se puede pasar una cancha, un cliente o dejar sin parametros
#centro.mostrarReservasTotales()

centro.consultaDisponible(4,2,17)


