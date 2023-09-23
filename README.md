# Proyecto de Gestión de Centros Deportivos

## Descripción
Este proyecto tiene como objetivo desarrollar un sistema de gestión para un centro deportivo. A continuación, se detallan los principales requerimientos y funcionalidades del sistema.

## Requerimientos Funcionales

### Canchas
- [x] Crear una cancha
- [x] Agregar una cancha en la lista de centros. No se podrá agregar si en la misma ya se encuentra registrada.
- [x] Listar las canchas totales según un tipo de deporte.
- [x] Quitar una cancha de la lista del centro. No se podrá quitar la cancha si la misma posee reservas pendientes.

### Clientes
- [x] Crear un cliente
- [x] Agregar un cliente en la lista del centro. No se podrá agregar si en la misma ya se encuentra registrado.
- [x] Quitar un cliente en la lista del centro. No se podrá quitar si el mismo tiene reservas pendientes.
- [x] Listar clientes morosos de una cancha o de la lista de clientes totales.

### Reservas
- [x] Crear una reserva. Para poder crear una reserva la cancha como el cliente deben estar habilitados, el horario correspondiente y además la cancha debe estar desocupada en ese horario. Al crear la reserva el cliente tendrá un movimiento negativo próximo a pagar.
- [x] Listar las reservas actuales, así como también las totales de una cancha dada, un cliente dado o totales.
- [x] Un cliente no puede reservar si tiene un saldo negativo menor a -2000.
- [x] Cada reserva generada el cliente tendrá un nuevo saldo negativo el cual será el costo de la misma.
- [x] El centro deberá registrar el pago del cliente aportando un movimiento positivo al mismo.
- [x] Mostrar saldo de un cliente.

### Empleados
- [x] Registrar un empleado a una cancha. Para esto la cancha debe estar habilitada y el empleado no debe estar registrado en ninguna otra cancha.
- [x] Asignar tarea a un empleado. El empleado deberá poder tener una lista de tareas, las mismas se pueden asignar y quitar. El empleado que no posee ninguna tarea estará como desocupado.
- [x] Listar los empleados que se encuentran desocupados.
- [x] Quitar un empleado de la cancha.
