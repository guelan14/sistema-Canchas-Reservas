# sistema-Canchas-Reservas
“Software Administrativo de Canchas”

Objetivo Principal: 
Simular una organización completa de un centro cuya función es el manejo de registros (empleados, clientes, reservas, canchas) y administración de tiempos y funciones para los mismos

Descripción:
El software se realizó con el objetivo de administrar o gestionar un año entero de un centro deportivo el cual consta con distintos tipos de cancha para su uso.
Un centro deportivo es un espacio el cual tiene como objetivo poder administrar adecuadamente horarios y reservas para sus canchas, como también gestionar sus empleados y clientes.
El mismo maneja conceptos tales como canchas, clientes, empleados, reservas, movimientos, tareas, entre otros.
Cada cliente es una persona, tiene un nombre, apellido, teléfono y edad. Este puede solicitar una reserva, cancelarla, entre otros. 
Los empleados por otro lado también son personas. Estos tienen tareas asignadas para le realización en la cancha donde se encuentran trabajando.
Las canchas pertenecientes al centro poseen un número, material, dirección. Los horarios de las canchas son de (8hs a 12hs) mañana y (19hs a 23hs) tarde. Estas tienen empleados y las reservas correspondientes a las mismas.
Las reservas tendrán información de la cancha, cliente, fecha y el día. Cada reserva tiene definido como tiempo predeterminado 1 hs. Cada cliente podrá reservar sin pagar hasta llegar al saldo máximo de deuda. 


 




REQUERIMIENTOS:
*	Crear una cancha
*	Agregar una cancha en la lista de centro. No se podrá agregar si en la misma ya se encuentra registrada.
*	Listar las canchas totales según un tipo de deporte.
*	Quitar una cancha de la lista del centro. No se podrá quitar la cancha si la misma posee reservas pendientes.
*	Crear un cliente
* Agregar un cliente en la lista del centro. No se podrá agregar si en la misma ya se encuentra registrado 
* Quitar un cliente en la lista del centro. No se podrá quitar si el mismo tiene reservas pendientes.
*	Crear una reserva. Para poder crear una reserva la cancha como el cliente deben estar habilitados, el horario correspondiente y además la cancha debe estar desocupada en ese horario. Al crear la reserva el cliente tendrá un movimiento negativo próximo a pagar.
*	Listar las reservas actuales, así como también las totales de una cancha dada, un cliente dado o totales.
*	Listar las canchas disponibles para una fecha dada y un deporte solicitado o si la misma recibe una cancha y una fecha saber si esta está disponible.
*	Un cliente no puede reservar si tiene un saldo negativo menor a -2000.
*	Cada reserva generada el cliente tendrá un nuevo saldo negativo el cual será el costo de la misma. 
*	El centro deberá registrar el pago del cliente aportando un movimiento positivo al mismo. 
*	Mostrar saldo de un cliente.
*	Listar clientes morosos de una cancha o de la lista de clientes totales.
*	Registrar un empleado a una cancha. Para esto la cancha debe estar habilitada y el empleado no debe estar registrado en ninguna otra cancha.
*	Asignar tarea a un empleado. El empleado deberá poder tener una lista de tareas, las mismas se pueden asignar y quitar. El empleado que no posee ninguna tarea estará como desocupado.
*	Listar los empleados que se encuentran desocupados.
*	Quitar un empleado de la cancha.
